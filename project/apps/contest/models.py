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
	owner = ReferenceField('User', required=True)
	name = StringField(required=True)
	starts_on = DateTimeField(required=True)
	duration = IntField(required=True)
	teams = ListField(EmbeddedDocumentField(TeamInfo))
	problems = ListField(EmbeddedDocumentField(Problem))
