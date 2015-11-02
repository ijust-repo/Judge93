# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# python imports
from mongoengine import Document, StringField, IntField, DateTimeField, ReferenceField, ListField, EmbeddedDocument, EmbeddedDocumentField


class TeamInfo(EmbeddedDocument):
	team = ReferenceField('Team', required=True)
	penalty = IntField()


class Contest(Document):
	owner = ReferenceField('User', required=True)
	name = StringField(required=True)
	start_time = DateTimeField(required=True)
	duration = IntField(required=True)
	teams = ListField(EmbeddedDocumentField(TeamInfo))
