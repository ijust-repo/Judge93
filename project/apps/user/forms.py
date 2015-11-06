# -*- coding: utf-8 -*-
__author__ = ['AminHP','SALAR']

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators


class Login(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])


class Signup(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])

class ChangePassword(Form):
    old_password = PasswordField(validators=[validators.DataRequired()])
    new_password = PasswordField(validators=[validators.DataRequired()])
