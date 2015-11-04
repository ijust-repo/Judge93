#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'AminHP'

#mongo import
from mongoengine import connect

# flask import
from flask import Flask, session, request
import wtforms_json

#project import
from project.apps.user import user
from project.apps.team import team
from project.apps.contest import contest
from project.utils.access import logged_in_user


def authenticate():
	without_login_url_list = ('static', 'user.login', 'user.exists', 'user.do_login', 'user.signup', 'user.do_signup')
	if request.endpoint not in without_login_url_list:
		if not logged_in_user():
			return "please login first", 405


def run():
	wtforms_json.init()
	connect('judge93')
	app = Flask('ElmosJudge93', static_folder='project/statics', 
			template_folder='project/templates')
	app.register_blueprint(user)
	app.register_blueprint(team)
	app.register_blueprint(contest)
	app.secret_key = '.g2He35T9TQhTxth3IPj75KP5zQDAmXaZWiVz1FwCKAWs3Oi'
	app.config["WTF_CSRF_ENABLED"] = False
	app.before_request(authenticate)
	app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
	run()
