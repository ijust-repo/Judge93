# -*- coding: utf-8 -*-
__author__ = 'Kia'

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, FloatField , DateTimeField, validators, FieldList, IntegerField, FormField


class CreateContest(Form):
	name = StringField(validators=[validators.DataRequired()])
	starts_on = FloatField(validators=[validators.DataRequired()])
	ends_on =  FloatField(validators=[validators.DataRequired()])


class TestCase (Form):
	input = StringField(validators=[validators.DataRequired()])
	output = StringField(validators=[validators.DataRequired()])


class AddProblem(Form):
	title = StringField (validators=[validators.DataRequired()])
	time_limit = IntegerField (validators=[validators.DataRequired()])
	space_limit = IntegerField (validators=[validators.DataRequired()])
	header = StringField ()
	body = StringField (validators=[validators.DataRequired()])
	testcases = FieldList(FormField(TestCase))
	footer = StringField ()