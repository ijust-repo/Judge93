# -*- coding: utf-8 -*-
__author__ = ['Kia' , 'mahnoosh','nargess',"Amin Hosseini"]



#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.team import team

from project.apps.team.forms import *
from project.utils.access import login_user, logout_user, logged_in_user

from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest

from mongoengine import DoesNotExist, NotUniqueError



@team.route('/', methods=['GET'])
def team_page():
        return render_template('team.html')


@team.route('create/', methods=['POST'])
def create():
        form = CreateTeam.from_json(request.json)
        if form.validate():
                name = form.data['name']
                members = form.data ['members']
                if (len(members) > 2) :
                        form.members.errors.append(form.members.gettext('Number of members must be under three!'))
                        return jsonify(errors=form.errors), 406
                try:
                        user_obj = User.objects().get(username=logged_in_user())
                        team_obj = Team(name=name)
                        team_obj.owner = user_obj
                        members_list = []
                        for i in members:
                                if (i == logged_in_user()):
                                        form.members.errors.append(form.members.gettext('Owner can not be added to the team!'))
                                        return jsonify(errors=form.errors), 406
                                if (User.objects().get(username=i) not in members_list):
                                        members_list.append (User.objects().get(username=i))
                                else:
                                        form.members.errors.append(form.members.gettext('No one can be added twice!'))
                                        return jsonify(errors=form.errors), 406
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
                        form.members.errors.append(form.members.gettext('User does not exist!'))
                        return jsonify(errors=form.errors), 406
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

        except DoesNotExist:
            form.name.errors.append(form.name.gettext('Team does not exist!'))
            return jsonify(errors=form.errors), 401

        if not team_obj.owner.username == logged_in_user():
                form.members.errors.append(form.members.gettext("you aren't team owner!"))
                return jsonify(errors=form.errors), 403
                
        if len(team_obj.members) + len(members) > 2:
            form.members.errors.append(form.members.gettext('Number of members must be under three!'))
            return jsonify(errors=form.errors), 406

        if logged_in_user() in members:
            form.members.errors.append(form.members.gettext('you already are in the team members remove yourself from the list!'))
            return jsonify(errors=form.errors), 401

        for member in members:
            if User.objects.get(username=member) in team_obj.members:
                form.members.errors.append(form.members.gettext('No one can be added twice!'))
                return jsonify(errors=form.errors), 401
            else:
                try:
                        u = User.objects.get(username=member)
                        team_obj.members.append(u)
                        u.teams.append(team_obj)
                        u.save()
                except DoesNotExist:
                        form.members.errors.append(form.members.gettext('User does not exist!'))
                        return jsonify(errors=form.errors), 406
                
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
			if obj.owner== logged_in_user():
				obj.name = new_name
				obj.save()
				return "" , 200
			else:
				
				return jsonify(errors="User is not owner"), 403
		
		except DoesNotExist:			
			return jsonify(errors='Team does not exist!'), 406
			
		except NotUniqueError:
			form.new_name.errors.append(form.new_name.gettext('This team name already exists.'))
			return jsonify(errors=form.errors), 409


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




			
