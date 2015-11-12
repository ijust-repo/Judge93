# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# python imports
from hashlib import sha384

from mongoengine import Document, StringField, ReferenceField, ListField


class User(Document):
	username = StringField(required=True, unique=True)
	password = StringField(required=True)
	email = StringField(required=True, unique=True)
	teams = ListField(ReferenceField('Team'))


	def set_password(self, password):
		self.password = sha384(password).hexdigest()

	def verify_password(self, password):
		return sha384(password).hexdigest() == self.password

	def change_password(self, old_password, new_password):
		if self.verify_password(old_password):
			self.password = sha384(new_password).hexdigest()
			return True
		return False

	def reset_password(self):
		self.password = None


	def to_json(self):
		return dict(
			id=str(self.pk),
			username=self.username)

	def to_json_profile(self):
		return dict(
			id=str(self.pk),
			username=self.username,
			email=self.email)
