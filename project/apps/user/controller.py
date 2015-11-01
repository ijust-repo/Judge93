# -*- coding: utf-8 -*-
__author__ = 'AminHP'


#flask import
from flask import request, render_template

#project import
from project.apps.user import user
from project.apps.user.forms import Login
from project.utils.access import login_user, logout_user


@user.route('login/', methods=['GET', 'POST'])
def login():
	form = Login()
	if request.method == 'POST':
		if form.validate_on_submit():
			login_user(form.username)
			return "success"
	return render_template('login.html', form=form)


@user.route('logout/', methods=['GET'])
def logout():
	logout_user()
	return render_template('logout.html')
