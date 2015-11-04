# -*- coding: utf-8 -*-
__author__ = 'AminHP & Kia'

# python imports
from mongoengine import Document, StringField, ReferenceField, ListField


class Team(Document):
	owner = ReferenceField('User', required=True)
	name = StringField(required=True, unique=True)
	members = ListField(ReferenceField('User'))
	contests = ListField(ReferenceField('Contest'))

	def set_name(self, name):
		self.name = name