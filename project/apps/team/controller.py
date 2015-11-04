# -*- coding: utf-8 -*-
__author__ = 'Kia'


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.team import team
from project.apps.team.forms import AddTeam
from project.utils.access import login_user, logout_user

from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest

from mongoengine import DoesNotExist, NotUniqueError



@team.route('add/', methods=['GET'])
def add():
	return render_template('add_team.html')


@user.route('add_request/<string:name>/', methods=['GET'])
def add_request(name):
	form = AddTeam.from_json(request.json)
	if form.validate():
		name = form.data['name']
	if form.validate_on_submit():
		try:
			#Team.objects().get(name=name)
			obj = team(name=name)
			obj.set_name(name)
			obj.save()
			return "", 200
		except NotUniqueError:
			return "", 409
		


