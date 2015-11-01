# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators


class Login(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])

