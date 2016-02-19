# -*- coding: utf-8 -*-
__author__ = ['Kia' , 'SALAR']

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, FloatField , DateTimeField, validators, FieldList, IntegerField, FormField, BooleanField


class CreateContest(Form):
	name = StringField(validators=[validators.DataRequired()])
	starts_on = FloatField(validators=[validators.DataRequired()])
	ends_on =  FloatField(validators=[validators.DataRequired()])

	def verify_name(self):
        	import re
        	if self.name.data == re.search('[\w.]*', self.name.data).group():
            		return True
        	return False


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


class EditTestCase (Form):
	id = IntegerField ()
	order = IntegerField ()
	input = StringField()
	output = StringField()

class EditProblem(Form):
	id = IntegerField ()
	order = IntegerField ()
	title = StringField ()
	time_limit = IntegerField ()
	space_limit = IntegerField ()
	header = StringField ()
	body = StringField ()
	testcases = FieldList(FormField(EditTestCase))
	footer = StringField ()

class EditContest(Form):
	problems = FieldList(FormField(EditProblem))
	name = StringField()
	starts_on = FloatField()
	ends_on = FloatField()

class AcceptTeam(Form):
	acceptation = BooleanField()