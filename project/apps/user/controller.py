# -*- coding: utf-8 -*-
__author__ = 'AminHP'


#flask import
from flask import request, render_template

#project import
from project.apps.user import user
from project.apps.user.forms import Login, Signup
from project.utils.access import login_user, logout_user

from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest

from mongoengine import DoesNotExist, NotUniqueError



@user.route('login/', methods=['GET', 'POST'])
def login():
	form = Login()
	if request.method == 'POST':
		username = form.data['username']
		password = form.data['password']
		if form.validate_on_submit():
			try:
				obj = User.objects().get(username=username)
				if obj.verify_password(password):
					login_user(username)
					return "success"
				else:
					return "wrong password"
			except DoesNotExist:
				return "user not found"
	return render_template('login.html', form=form)


@user.route('signup/', methods=['GET', 'POST'])
def signup():
	form = Signup()
	if request.method == 'POST':
		username = form.data['username']
		password = form.data['password']
		if form.validate_on_submit():
			try:
				obj = User(username=username)
				obj.set_password(password)
				obj.save()
			except NotUniqueError:
				return "user already exists"
			return "success"
	return render_template('signup.html', form=form)


@user.route('logout/', methods=['GET'])
def logout():
	logout_user()
	return render_template('logout.html')
