# -*- coding: utf-8 -*-
__author__ = ['AminHP','SALAR', 'mahnoosh', 'Aref']


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.user.forms import Login, Signup, ChangePassword, ChangeProfile
from project.utils.access import login_user, logout_user ,logged_in_user
from project.utils.date import datetime_to_str

#models import
from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest

#other
from mongoengine import DoesNotExist, NotUniqueError

@user.route('/', methods=['GET'])
def user_page():
	return render_template('user.html')
		
@user.route('<string:Username>/', methods=['GET'])
def user_home_page(Username):
	try:
		obj = User.objects().get(username = Username)	
		pk = obj.pk
		return render_template("home.html" , user_id=pk)  
	except DoesNotExist:
		return 	jsonify(errors="User does not exists!"), 406

@user.route('<string:Username>/contest/', methods=['GET'])
def user_contest_page(Username):
	try:
		obj = User.objects().get(username=Username)
		pk = obj.pk
		return render_template('contest.html' , user_id = pk)
	except DoesNotExist:
		return 	jsonify(errors="User does not exists!"), 406

@user.route('setting/', methods=['GET'])
def user_setting_page():
	return render_template('setting.html')

@user.route('<string:Username>/team/', methods=['GET'])
def user_team_page(Username):
	try:
		obj = User.objects().get(username = Username)
		pk = obj.pk
		return render_template('team.html' , user_id = pk)
	except DoesNotExist:
		return jsonify(errors="User does not exists!"), 406

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
		email = form.data['email']
		password = form.data['password']
		if form.validate_on_submit():
			try:
				obj = User(username=username, email=email)
				obj.set_password(password)
				obj.save()
			except NotUniqueError, err:
				err = err.args[0]
				if '$username' in err:
					form.username.errors.append(form.username.gettext('Username already exists.'))
				elif '$email' in err:
					form.email.errors.append(form.email.gettext('Email already exists.'))
				return jsonify(errors=form.errors), 409
			return "", 201
	return "", 406


@user.route('logout/', methods=['GET'])
def logout():
	logout_user()
	return "", 200


@user.route('change_profile/', methods=['PUT'])
def change_profile():
	form = ChangeProfile.from_json(request.json)
	if form.validate():
		past_username = logged_in_user()
		new_username = form.data['new_username']
		new_email = form.data['new_email']
		obj = User.objects().get(username=past_username)
		try:
			if new_username:
				obj.username = new_username
			if new_email:
				obj.email = new_email
			obj.save()
			return "", 200
		except NotUniqueError, err:
			err = err.args[0]
			if '$username' in err:        
				form.new_username.errors.append(form.new_username.gettext('Username already exist.'))
			elif '$email' in err:
				form.new_email.errors.append(form.new_email.gettext('Email already exist.'))
			return jsonify(errors=form.errors), 409
	return "", 406


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

                        
@user.route('get_profile/by_username/<string:username>/', methods=['GET'])
def get_user_profile_by_username(username):
	try:
		obj = User.objects().get(username=username)
		resp = obj.to_json_profile()
		resp.pop('username', None)
		return jsonify(resp), 200
	except DoesNotExist:
		return jsonify(errors="User does not exists!"), 406


@user.route('get_profile/by_id/<string:user_id>/', methods=['GET'])
def get_user_profile_by_id(user_id):
	try:
		obj = User.objects().get(pk=user_id)
		resp = obj.to_json_profile()
		resp.pop('id', None)
		return jsonify(resp), 200
	except DoesNotExist:
		return jsonify(errors="User does not exists!"), 406
		
			
@user.route('get_profile/', methods=['GET'])
def get_current_user():
	
	obj = User.objects().get(username=logged_in_user())
	resp = obj.to_json_profile()
	return jsonify(resp) ,200
	

@user.route('<string:user_id>/teams/', methods=['GET'])
def get_users_teams(user_id):
	try:
		obj = User.objects().get(pk=user_id)
		teams = obj.teams		
		resp = []
		
		for team in teams:
			contests = team.contests		
			members = team.members
			contests_list =[]	
			team_info = {}
			members_list = []
			
			for member in members:
				members_list.append(member.to_json())
			
			for contest in contests:
				contests_info = {}
				contests_info ["name"] = contest.name
				contests_info ["id"] = str(contest.pk)
				contests_info ["start_on"] = datetime_to_str(contest.starts_on)
				contests_info ["ends_on"] = datetime_to_str(contests.ends_on)
				contests_list.append(contests_info)				
			
			team_info["contests"] = contests_list
			team_info["id"]= str(team.pk)	
			team_info["name"]= team.name
			team_info["owner"] = team.owner.to_json()	
			team_info["members"] = members_list			
			
			resp.append(team_info)

		return jsonify(teams=resp),200
	except DoesNotExist:
		return jsonify(errors="User does not exists!"), 406
	
