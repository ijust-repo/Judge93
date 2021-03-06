# -*- coding: utf-8 -*-
__author__ = ['Kia' , 'mahnoosh','nargess',"Amin Hosseini", 'AminHP', "SALAR"]

#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.team import team

from project.apps.team.forms import *
from project.utils.access import login_user, logout_user, logged_in_user

#models import
from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest, TeamInfo

#other
from datetime import datetime
from mongoengine import DoesNotExist, NotUniqueError
from copy import copy

def running_contests(team_obj):
	started_contests=[]
	for contest in team_obj.contests:
		if contest.starts_on < datetime.utcnow() and datetime.utcnow() < contest.ends_on:
			return True
	return False



@team.route('team/', methods=['GET'])
def team_team_page():
	return render_template('team.html')


@team.route('<string:team_name>/', methods=['GET'])
def team_page(team_name):
	try:
		obj = Team.objects().get(name = team_name)
		pk = obj.pk
		return render_template('team.html' , team_id = pk)
	except DoesNotExist:
		return jsonify(errors="team does not exists!"), 406

@team.route('create/', methods=['POST'])
def create():
	form = CreateTeam.from_json(request.json)
	if form.validate():
		name = form.data['name']
		members = form.data ['members']
		if not form.verify_name():
			return jsonify(errors='Team name may only contain alphanumeric characters, "_" or "."'), 406
		if (len(members) > 2) :
			return jsonify(errors='Number of members must be under three!'), 406
		try:
			user_obj = User.objects().get(username=logged_in_user())
			if len(user_obj.teams) > 1:
				return jsonify(errors='You cannot create more teams!'), 406

			team_obj = Team(name=name)
			team_obj.owner = user_obj
			members_list = []
			for i in members:
				if (i == logged_in_user()):
					return jsonify(errors='Owner can not be added to the team!'), 406
				if (User.objects().get(username=i) not in members_list):
					members_list.append (User.objects().get(username=i))
				else:
					return jsonify(errors='No one can be added twice!'), 406
			team_obj.members = members_list
			team_obj.save()
			user_obj.teams.append (team_obj)
			user_obj.save()
			for i in members:
				user_obj = User.objects().get(username=i)
				user_obj.teams.append (team_obj)
				user_obj.save()
			return "", 201
		except DoesNotExist:
			return jsonify(errors='User does not exist!'), 406
		except NotUniqueError:
			return "", 409
	return "", 406


@team.route('members/',methods=['POST'])
def add_member():
	form = AddMember.from_json(request.json)
	if form.validate():
		name = logged_in_user()
		team_name = form.data['name']
		members = form.data ['members']
		try:
			team_obj = Team.objects.get(name=team_name)
			if running_contests(team_obj):
				return jsonify(errors="you are in a running contest") , 403

		except DoesNotExist:
			return jsonify(errors='Team does not exists!'), 406

		if not team_obj.owner.username == logged_in_user():
			return jsonify(errors="you aren't team owner!"), 403

		if len(team_obj.members) + len(members) > 2:
			return jsonify(errors='Number of members must be under three!'), 406

		if logged_in_user() in members:
			return jsonify(errors='you already are in the team members remove yourself from the list!'), 406

		for member in members:
			try:
				user_obj = User.objects.get(username=member)
			except DoesNotExist:
				return jsonify(errors='User does not exist!'), 406
			if user_obj in team_obj.members:
				return jsonify(errors='No one can be added twice!'), 406
			else:
				team_obj.members.append(user_obj)
				user_obj.teams.append(team_obj)
				user_obj.save()
				team_obj.save()
		return "",200
	else:
		return "",406


@team.route('change_name/<string:team_id>/', methods=['PUT'])
def change_team_name(team_id):
	form = ChangeName.from_json(request.json)
	if form.validate():
		new_name = form.data['new_name']
		try:
			obj = Team.objects().get(pk=team_id)
			if running_contests(obj):
				return jsonify(errors="you are in a running contest") , 403

			if obj.owner.username == logged_in_user():
				obj.name = new_name
				obj.save()
				return "" , 200
			else:

				return jsonify(errors="User is not owner"), 403

		except DoesNotExist:
			return jsonify(errors='Team does not exist!'), 406

		except NotUniqueError:
			return jsonify(errors='This team name already exists.'), 409


	return "" , 406


@team.route('members/<string:team_id>/', methods=['GET'])
def get_team_member(team_id):
	try:
		team_obj = Team.objects().get(pk=team_id)
		members_list=[]
		members_list.append(team_obj.owner.to_json())
		for i in team_obj.members :
			members_list.append(i.to_json())
		return jsonify(members=members_list),200

	except DoesNotExist:
		return jsonify(errors='Team does not exist!'), 406


@team.route('<string:team_id>/info/', methods=['GET'])
def get_team_info(team_id):
	try:
		team_obj = Team.objects().get(pk=team_id)
		res = {}
		res['name'] = team_obj.name
		res['owner'] = team_obj.owner.to_json()
		res['members'] = [member.to_json() for member in team_obj.members]
		res['contests'] = []

		for accepted_contest in team_obj.contests:
			temp_dict ={}
			temp_dict["name"]=accepted_contest.name
			temp_dict["status"]="accepted"
			res["contests"].append(temp_dict)

		for pending_contest in team_obj.pending_contests:
			temp_dict ={}
			temp_dict["name"]=pending_contest.name
			temp_dict["status"]="pending"
			res["contests"].append(temp_dict)

		for rejected_contest in team_obj.rejected_contests:
			temp_dict ={}
			temp_dict["name"]=rejected_contest.name
			temp_dict["status"]="rejected"
			res["contests"].append(temp_dict)

		return jsonify(res), 200

	except DoesNotExist:
		return jsonify(errors='Team does not exist!'), 406


@team.route('join_request/', methods=['POST'])
def join_request():
	form = JoinRequest.from_json(request.json)
	if form.validate():
		contest_id = form.data['contest_id']
		team_name = form.data['team_name']
		
		try:
			contest_obj = Contest.objects().get(pk=contest_id)
			team_obj = Team.objects().get(name=team_name)
			if logged_in_user() != team_obj.owner.username:
				return jsonify(errors = "user is not team owner") , 403
				
			if contest_obj.ends_on < datetime.utcnow():
				return jsonify(errors = "this contest has been finished") , 403

			team_members_with_owner = copy(team_obj.members)
			team_members_with_owner.append(team_obj.owner)

			for info in contest_obj.teams:
				if (team_obj == info.team):

					if (info.accepted == False):
						info.accepted = None
						team_obj.pending_contests.append(contest_obj)
						team_obj.update(pull__rejected_contests=contest_obj)
						contest_obj.save()
						team_obj.save()
						return jsonify(errors = "join request not accepted -> Re_sent") , 200

					elif (info.accepted == True):
						return jsonify(errors = 'team already exists in contest!'), 409

					else:
						return jsonify(errors = " please wait for checking your join request") , 406

				contest_teams_members_with_owner = info.team.members
				contest_teams_members_with_owner.append(info.team.owner)
				for member in contest_teams_members_with_owner:
					if (member in team_members_with_owner):
						return jsonify(errors = 'user %s is in contest' %member.username), 409

			team_obj.pending_contests.append(contest_obj)
			team_info = TeamInfo (team = team_obj)
			contest_obj.teams.append(team_info)
			contest_obj.save()
			team_obj.save()
			return "" , 200

		except DoesNotExist:
			return jsonify(errors="Contest or Team does not exist!") , 406

@team.route('<string:team_id>/member/<string:member_id>/', methods=['DELETE'])
def remove_member(team_id, member_id):
	try:
		team = Team.objects().get(pk=team_id)
		if running_contests(team):
			return jsonify(errors="you are in a running contest") , 403

		if logged_in_user() != team.owner.username:
			return jsonify(errors="User is not owner"), 403

		member = User.objects().get(pk=member_id)
		team.update(pull__members=member)
		member.update(pull__teams=team)
		team.save()
		member.save()

		return "", 200
	except DoesNotExist:
		return jsonify(errors='Team or member does not exist!'), 406
