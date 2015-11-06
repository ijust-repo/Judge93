# -*- coding: utf-8 -*-
__author__ = ['AminHP','SALAR']


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.user.forms import Login, Signup , ChangePassword
from project.utils.access import login_user, logout_user ,logged_in_user

from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest

from mongoengine import DoesNotExist, NotUniqueError



@user.route('/', methods=['GET'])
def user_page():
	return render_template('user.html')


@user.route('home/', methods=['GET'])
def user_home_page():
	return render_template('home.html')


@user.route('exists/<string:username>/', methods=['GET'])
def exists(username):
	try:
		User.objects().get(username=username)
	except DoesNotExist:
		return "", 404
	return "", 200


@user.route('login/', methods=['POST'])
def login():
	form = Login.from_json(request.json)
	if form.validate():
		username = form.data['username']
		password = form.data['password']
		try:
			obj = User.objects().get(username=username)
			if obj.verify_password(password):
				login_user(username)
				return "", 200
			else:
				form.password.errors.append(form.password.gettext('Wrong password.'))
				return jsonify(errors=form.errors), 401
		except DoesNotExist:
			form.username.errors.append(form.username.gettext('Username does not exists.'))
			return jsonify(errors=form.errors), 401
	return "", 406



@user.route('signup/', methods=['POST'])
def signup():
	form = Signup.from_json(request.json)
	if form.validate():
		username = form.data['username']
		password = form.data['password']
		if form.validate_on_submit():
			try:
				obj = User(username=username)
				obj.set_password(password)
				obj.save()
			except NotUniqueError:
				form.username.errors.append(form.username.gettext('Username already exists.'))
				return jsonify(errors=form.errors), 409
			return "", 201
	return "", 406


@user.route('logout/', methods=['GET'])
def logout():
	logout_user()
	return "", 200


@user.route('change_password/', methods=['PUT'])
def change_password():
        form = ChangePassword.from_json(request.json)
        if form.validate():
                old_password = form.data['old_password']
                new_password = form.data['new_password']
                username = logged_in_user()
                obj = User.objects().get(username=username)
                if obj.change_password(old_password , new_password):
                        obj.save()
                        return "", 200
                else:
                        form.old_password.errors.append(form.old_password.gettext('Wrong password.'))
                        return jsonify(errors=form.errors), 401
        return "", 406
                        
