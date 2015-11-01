# -*- coding: utf-8 -*-
__author__ = 'AminHP'


#flask import
from flask import request, session, render_template

#project import
from project.apps.user import user
from project.apps.user.forms import Login


@user.route('login/', methods=['GET', 'POST'])
def login():
	form = Login()
	if request.method == 'POST':
		if form.validate_on_submit():
			session['username'] = form.username
			return "success"
	return render_template('login.html', form=form)


@user.route('logout/', methods=['GET'])
def logout():
	session.pop('username')
	return render_template('logout.html')
