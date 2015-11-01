#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'AminHP'


# flask import
from flask import Flask, session, request

#project import
from project.apps.user import user
from project.utils.access import logged_in_user


def authenticate():
	without_login_url_list = ('static', 'user.login', 'user.signup')
	if request.endpoint not in without_login_url_list:
		if not logged_in_user():
			return "please login first"


def run():
	app = Flask('ElmosJudge93', static_folder='project/statics', 
			template_folder='project/templates')
	app.register_blueprint(user)
	app.secret_key = '.g2He35T9TQhTxth3IPj75KP5zQDAmXaZWiVz1FwCKAWs3Oi'
	app.before_request(authenticate)
	app.run(host='0.0.0.0')


if __name__ == '__main__':
	run()
