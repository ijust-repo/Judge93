# -*- coding: utf-8 -*-
__author__ = 'Kia'

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, validators


class AddTeam(Form):
    name = StringField(validators=[validators.DataRequired()])
