# -*- coding: utf-8 -*-
__author__ = 'AminHP'


#flask import
from flask import session


def login_user(username):
	session['username'] = username

def logout_user():
	session.pop('username')

def logged_in_user():
	return session.get('username', None)
