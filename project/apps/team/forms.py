# -*- coding: utf-8 -*-
__author__ = ['Kia' , 'mahnoosh','Amin Hosseini','SALAR']

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField,SelectMultipleField, validators, FieldList

class CreateTeam(Form):
	name = StringField(validators=[validators.DataRequired()])
	members = FieldList(StringField())

class AddMember(Form):
        name    = StringField(validators=[validators.DataRequired()])
        members = FieldList(StringField())

class ChangeName(Form):
	new_name = StringField(validators=[validators.DataRequired()])

class JoinRequest(Form):
	contest_id = StringField(validators=[validators.DataRequired()])
	team_id    = StringField(validators=[validators.DataRequired()])