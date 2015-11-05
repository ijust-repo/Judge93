# -*- coding: utf-8 -*-
__author__ = 'Kia'


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.team import team
from project.apps.team.forms import CreateTeam
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
			return jsonify(errors=form.errors), 401
			#return "", 401
		try:
			user_obj = User.objects().get(username=logged_in_user())
			team_obj = Team(name=name)
			team_obj.owner = user_obj
			members_list = [user_obj]
			for i in members:
				if (i == logged_in_user()):
					form.members.errors.append(form.members.gettext('Owner is one of members by default!'))
					return jsonify(errors=form.errors), 401
				if (User.objects().get(username=i) not in members_list):

					members_list.append (User.objects().get(username=i))
				else:

					form.members.errors.append(form.members.gettext('No one can be added twice!'))
					return jsonify(errors=form.errors), 401
			user_obj.teams.append (team_obj)
			user_obj.save()
			for i in members:
				user_obj = User.objects().get(username=i)
				user_obj.teams.append (team_obj)
				user_obj.save()
			team_obj.members = members_list
			team_obj.save()
			return "", 201
		except DoesNotExist:
			form.members.errors.append(form.members.gettext('User does not exist!'))
			return jsonify(errors=form.errors), 401
			#return "", 410
		except NotUniqueError:
			return "", 409

	return "", 406
			


