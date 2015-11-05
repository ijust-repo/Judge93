# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField


class Login(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])


class Signup(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])


class ChangeUser(Form):
    username = StringField()
    email = StringField()
    
