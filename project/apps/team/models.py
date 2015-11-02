# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# python imports
from mongoengine import Document, StringField, ReferenceField, ListField


class Team(Document):
	owner = ReferenceField('User', required=True)
	name = StringField(required=True)
	members = ListField(ReferenceField('User'))
	contests = ListField(ReferenceField('Contest'))


	def __init__(self):
		self.members = []
