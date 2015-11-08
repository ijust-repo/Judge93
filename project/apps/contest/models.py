# -*- coding: utf-8 -*-
__author__ = ['AminHP', 'Kia']

# python imports
from mongoengine import Document, StringField, IntField, BooleanField, DateTimeField, ReferenceField, ListField, EmbeddedDocument, EmbeddedDocumentField

# project imports
from project.utils.date import datetime_to_str



class Testcase(EmbeddedDocument):
	id = IntField(required=True, unique=True)
	order = IntField(required=True, unique=True, sparse=True)
	input = StringField(required=True)
	output = StringField(required=True)


class Problem(EmbeddedDocument):
	id = IntField(required=True, unique=True)
	order = IntField(required=True, unique=True, sparse=True)
	title = StringField(required=True)
	time_limit = IntField(required=True)
	space_limit = IntField(required=True)
	header = StringField()
	body = StringField(required=True)
	testcases = ListField(EmbeddedDocumentField(Testcase))
	footer = StringField()



class Result(EmbeddedDocument):
	id = IntField(required=True, unique=True)
	problem = ReferenceField('Problem', required=True, unique=True, sparse=True)
	status = StringField()
	penalty = IntField()
	solved = BooleanField()


class TeamInfo(EmbeddedDocument):
	id = IntField(required=True, unique=True)
	team = ReferenceField('Team', required=True, unique=True, sparse=True)
	accepted = BooleanField()
	problem_results = ListField(EmbeddedDocumentField(Result))



class Contest(Document):
	name = StringField(required=True, unique=True)
	owner = ReferenceField('User', required=True)
	created_on = DateTimeField(required=True)
	starts_on = DateTimeField(required=True)
	ends_on = DateTimeField(required=True)
	problems = ListField(EmbeddedDocumentField(Problem))
	teams = ListField(EmbeddedDocumentField(TeamInfo))

	def to_json(self):
		return dict(
			id=str(self.pk),
			name=self.name,
			owner=self.owner.to_json(),
			created_on=datetime_to_str(self.created_on),
			starts_on=datetime_to_str(self.starts_on),
			ends_on=datetime_to_str(self.ends_on))
