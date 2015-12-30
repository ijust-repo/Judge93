#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = ['AminHP','SALAR']

#python import
import sys
import subprocess


def run_test():
	from werkzeug.serving import make_ssl_devcert

	#project import
	from project.apps.user import user
	from project.apps.team import team
	from project.apps.contest import contest
	from project.utils.access import logged_in_user
	from mongoengine import connect

	# flask import
	from flask import Flask, session, request, redirect, url_for, abort
	import wtforms_json
	from flask_limiter import Limiter


	def authenticate():
		if not request.endpoint:
			return "ERROR 404", 404
		without_login_url_list = ('static', 'index', 'user.user_page', 'user.login', 'user.exists', 'user.signup', 'user.forgot_password')
		if request.endpoint not in without_login_url_list:
			if not logged_in_user():
				return "ERROR 405", 405

	def limit_remote_addr():
		blocked_addr = []
		if request.remote_addr in blocked_addr:
			abort(403)  # Forbidden

	wtforms_json.init()
	connect('judge93')
	app = Flask('ElmosJudge93', static_folder='project/statics', 
			template_folder='project/templates')
	limiter = Limiter(app, global_limits=["30 per minute", "3 per second"])

	app.register_blueprint(user)
	app.register_blueprint(team)
	app.register_blueprint(contest)
	app.secret_key = '.g2He35T9TQhTxth3IPj75KP5zQDAmXaZWiVz1FwCKAWs3Oi'
	app.config['WTF_CSRF_ENABLED'] = False
	app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
	app.before_request(authenticate)
	app.before_request(limit_remote_addr)

	@app.route('/')
	def index():
		user = logged_in_user()
		if user:
			return redirect(url_for('user.user_home_page', Username=user))
		return redirect(url_for('user.user_page'))

	#make_ssl_devcert('key', host='0.0.0.0')
	#app.run(host='0.0.0.0', debug=True, ssl_context=('key.crt','key.key'))
	app.run(host='0.0.0.0', debug=True)


def help():
	print('''
Judge93 Project
python run.py [COMMAND]
COMMAND:
	test
		run judge93 app in test and debug mode.

	update_packages
		update project packages using python pip.

		'''
		  )


if __name__ == '__main__':
	if len(sys.argv) > 1:
		arg = (sys.argv[1])
		if arg == 'test':
			run_test()
		elif arg == 'update_packages':
			subprocess.call(['pip', 'install', '-r', 'requirements'])
		else:
			help()
	else:
		help()
