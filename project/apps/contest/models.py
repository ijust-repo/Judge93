# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# python imports
from mongoengine import Document, StringField, IntField, BooleanField, DateTimeField, ReferenceField, ListField, EmbeddedDocument, EmbeddedDocumentField


class Testcase(EmbeddedDocument):
	order = IntField(required=True, unique=True)
	input = StringField(required=True)
	output = StringField(required=True)


class Problem(EmbeddedDocument):
	order = IntField(required=True, unique=True)
	title = StringField(required=True)
	time_limit = IntField(required=True)
	space_limit = IntField(required=True)
	header = StringField()
	body = StringField(required=True)
	testcases = ListField(EmbeddedDocumentField(Testcase))
	footer = StringField()



class Result(EmbeddedDocument):
	problem = ReferenceField('Problem', required=True, unique=True)
	status = StringField()
	penalty = IntField()
	solved = BooleanField()


class TeamInfo(EmbeddedDocument):
	team = ReferenceField('Team', required=True, unique=True)
	problem_results = ListField(EmbeddedDocumentField(Result))



class Contest(Document):
	name = StringField(required=True, unique=True)
	owner = ReferenceField('User', required=True)
	created_on = DateTimeField(required=True)
	starts_on = DateTimeField(required=True)
	duration = IntField(required=True)
	problems = ListField(EmbeddedDocumentField(Problem))
	teams = ListField(EmbeddedDocumentField(TeamInfo))
