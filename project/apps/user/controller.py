# -*- coding: utf-8 -*-
__author__ = ['AminHP','SALAR', 'mahnoosh', 'Aref','narges']


#flask import
from flask import jsonify, request, render_template
import uuid,smtplib
#project import
from project.apps.user import user
from project.apps.user.forms import Login, Signup, ChangePassword, ChangeProfile ,ForgotPassword
from project.utils.access import login_user, logout_user ,logged_in_user
from project.utils.date import datetime_to_str
import project.config as config


#models import
from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest

#other
from mongoengine import DoesNotExist, NotUniqueError

@user.route('/', methods=['GET'])
def user_page():
	return render_template('user.html', site_key=config.site_key)
		
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
				return jsonify(errors='Wrong password.'), 401
		except DoesNotExist:
			return jsonify(errors='Username does not exists.'), 401
	return "", 406


@user.route('signup/', methods=['POST'])
def signup():
	form = Signup.from_json(request.json)
	if form.validate():
		username = form.data['username']
		email = form.data['email']
		password = form.data['password']
		recaptcha = form.data['recaptcha']
		if not form.verify_username():
			return jsonify(errors='Username may only contain alphanumeric characters, "_" or "."'), 406
		if form.verify_captcha(recaptcha):
			try:
				obj = User(username=username, email=email)
				obj.set_password(password)
				obj.save()
			except NotUniqueError, err:
				err = err.args[0]
				if '$username' in err:
					return jsonify(errors='Username already exists.'), 409
				elif '$email' in err:
					return jsonify(errors='Email already exists.'), 409
			return "", 201
		else:
			return jsonify(errors='Wrong captcha.'), 406
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
			logout_user()
			login_user(new_username)
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
			return jsonify(errors='Wrong password.'), 401
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
		
		for team_obj in teams:		
			team_info = team_obj.to_json_complete()
			team_info["contests"]=[]
			
			for accepted_contest in team_obj.contests:
				temp_dict ={}
				temp_dict["name"]=accepted_contest.name
				temp_dict["status"]="accepted"
				team_info["contests"].append(temp_dict)

			for pending_contest in team_obj.pending_contests:
				temp_dict ={}
				temp_dict["name"]=pending_contest.name
				temp_dict["status"]="pending"
				team_info["contests"].append(temp_dict)

			for rejected_contest in team_obj.rejected_contests:
				temp_dict ={}
				temp_dict["name"]=rejected_contest.name
				temp_dict["status"]="rejected"
				team_info["contests"].append(temp_dict)
			
			resp.append(team_info)

		return jsonify(teams=resp),200
	except DoesNotExist:
		return jsonify(errors="User does not exists!"), 406
	

@user.route('<string:user_id>/contest/<string:contest_id>/', methods=['GET'])
def get_user_team(user_id,contest_id):
	try:
		user_obj = User.objects().get(pk=user_id)
		contest_obj = Contest.objects().get(pk=contest_id)

		for info in contest_obj.teams:
			if (info.team.owner == user_obj) or (user_obj in info.team.members):
				return jsonify(info.team.to_json()) , 200
				
		return jsonify(errors="user is not in contest!") , 406
	except DoesNotExist:
		return jsonify(errors="user or contest does not exists!") , 406


@user.route('forgot_password/', methods=['POST'])

def forgot_password():
        form = ForgotPassword.from_json(request.json)
        if form.validate():
                username = form.data['username']
                email = form.data['email']
                try:
                        if username:
				if email:
					try:
						obj = User.objects().get(username=username , email=email )				
						sendmail(obj)
                      				return "", 200
                			except DoesNotExist:
						return 	jsonify(errors="Username or email does not exists!"), 406
				else :
					try:
						obj = User.objects().get(username=username)
                        	        	sendmail(obj)
                      				return "", 200
                			except DoesNotExist:
						return 	jsonify(errors="User does not exists!"), 406
			if email:
				try:
					obj = User.objects().get(email=email)
					sendmail(obj)
                      			return "", 200
                		except DoesNotExist:
					return 	jsonify(errors="Email does not exists!"), 406 
				


		except:                      
			return "", 406
        
def sendmail(obj):
	obj.reset_password()
	random = str(uuid.uuid4())
   	random = random.upper() 
   	random = random.replace("-","") 
 	new_password= random[0:6] 
	obj.set_password(new_password)
        obj.save()
	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo()
	session.starttls()
	session.login('iustjudge@gmail.com','iustjudge93')
	headers = "\r\n".join(["from: " + 'iustjudge@gmail.comm',
                       		"subject: " + "reset_password",
                     		"to: " + obj.email,
                       		"mime-version: 1.0",
                       		"content-type: text/html"])                  
	content = headers + "\r\n\r\n" + "Hi"+"\r\n\r\n"+" the new password is  "+new_password
	session.sendmail('iustjudge@gmail.com',obj.email, content)

