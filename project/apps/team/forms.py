# -*- coding: utf-8 -*-
__author__ = 'Kia' , 'mahnoosh'

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField,SelectMultipleField, validators, FieldList


class CreateTeam(Form):
	name = StringField(validators=[validators.DataRequired()])
	members = FieldList(StringField())
	
	
class ChangeName(Form):
	current_name = StringField(validators=[validators.DataRequired()])
	new_name =  StringField(validators=[validators.DataRequired()])
