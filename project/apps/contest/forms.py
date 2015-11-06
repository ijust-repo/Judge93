# -*- coding: utf-8 -*-
__author__ = 'Kia'

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, FloatField , DateTimeField, validators, FieldList


class CreateContest(Form):
	name = StringField(validators=[validators.DataRequired()])
	starts_on = FloatField(validators=[validators.DataRequired()])
	ends_on =  FloatField(validators=[validators.DataRequired()])
