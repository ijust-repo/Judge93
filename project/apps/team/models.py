# -*- coding: utf-8 -*-
__author__ = 'Amin HP'

# python imports
from mongoengine import Document, StringField, ReferenceField, ListField


class Team(Document):
	name = StringField(required=True, unique=True)
	owner = ReferenceField('User', required=True)
	members = ListField(ReferenceField('User'))
	contests = ListField(ReferenceField('Contest'))

	def to_json(self):
		return dict(
			id=str(self.pk),
			name=self.name,
			owner=self.owner.to_json())
;