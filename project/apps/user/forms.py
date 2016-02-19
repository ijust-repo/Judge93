# -*- coding: utf-8 -*-
__author__ = ['AminHP','SALAR','Aref','narges']

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators
import urllib, urllib2
import json

# project imports
import project.config as config


class Login(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])


class Signup(Form):
    username = StringField(validators=[validators.DataRequired()])
    email = StringField(validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField(validators=[validators.DataRequired()])
    recaptcha = StringField(validators=[validators.DataRequired()])

    @staticmethod
    def verify_captcha(recaptcha):
        post_data = {'secret': config.secret_key, 'response': recaptcha}
        result = urllib2.urlopen('https://www.google.com/recaptcha/api/siteverify', urllib.urlencode(post_data))
        resp = result.read()
        if not 'true' in resp:
            return False
        return True

    def verify_username(self):
        import re
        if self.username.data == re.search('[\w.]*', self.username.data).group():
            return True
        return False


class ChangeProfile(Form):
    new_username = StringField()
    new_email = StringField()


class ChangePassword(Form):
    old_password = PasswordField(validators=[validators.DataRequired()])
    new_password = PasswordField(validators=[validators.DataRequired()])

class ForgotPassword(Form):
    username = StringField()
    email = StringField()

