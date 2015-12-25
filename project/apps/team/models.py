# -*- coding: utf-8 -*-
__author__ = ['AminHP' , "SALAR"]

# python imports
from mongoengine import Document, StringField, ReferenceField, ListField


class Team(Document):
	name = StringField(required=True, unique=True)
	owner = ReferenceField('User', required=True)
	members = ListField(ReferenceField('User'))
	contests = ListField(ReferenceField('Contest'))
	pending_contests = ListField(ReferenceField('Contest'))
	rejected_contests = ListField(ReferenceField('Contest'))

	def to_json(self):
		return dict(
			id=str(self.pk),
			name=self.name,
			owner=self.owner.to_json())

	def to_json_complete(self):
		members_list=[]
		for user in self.members:
			members_list.append(user.to_json())
		return dict(
			id=str(self.pk),
			name=self.name,
			owner=self.owner.to_json(),
			members=members_list)