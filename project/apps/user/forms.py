# -*- coding: utf-8 -*-
__author__ = ['AminHP','SALAR','Aref']

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators


class Login(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])


class Signup(Form):
    username = StringField(validators=[validators.DataRequired()])
    email = StringField(validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField(validators=[validators.DataRequired()])


class ChangeProfile(Form):
    new_username = StringField()
    new_email = StringField()


class ChangePassword(Form):
    old_password = PasswordField(validators=[validators.DataRequired()])
    new_password = PasswordField(validators=[validators.DataRequired()])

class ForgotPassword(Form):
    username = StringField()
    email = StringField()

