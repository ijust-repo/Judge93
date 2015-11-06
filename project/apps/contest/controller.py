# -*- coding: utf-8 -*-
__author__ = 'Kia'


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.team import team
from project.apps.contest import contest
from project.apps.contest.forms import CreateContest, AddProblem
from project.utils.access import login_user, logout_user, logged_in_user
from project.utils.date import datetime_to_str, str_to_datetime
#models import
from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest, Problem, Testcase
#other
from datetime import datetime
from mongoengine import DoesNotExist, NotUniqueError


@contest.route('create/', methods=['POST'])
def create():
	form = CreateContest.from_json(request.json)
	if form.validate():
		name = form.data['name']
		starts_on = form.data ['starts_on']
		ends_on = form.data ['ends_on']
		if (starts_on > ends_on) :
			form.starts_on.errors.append(form.starts_on.gettext('Start date must be earlier than end date!'))
			return jsonify(errors=form.errors), 406
		if (datetime.utcnow() > datetime.fromtimestamp(starts_on) ) :
			form.starts_on.errors.append(form.starts_on.gettext('Start date must be later than now!'))
			return jsonify(errors=form.errors), 406
		try:
			contest_obj = Contest(name=name)
			contest_obj.owner = User.objects().get(username=logged_in_user())
			contest_obj.starts_on = datetime.fromtimestamp(starts_on)
			contest_obj.ends_on = datetime.fromtimestamp(ends_on)
			contest_obj.created_on = datetime.utcnow()
			contest_obj.save()
			return "", 201
		except NotUniqueError:
			form.name.errors.append(form.name.gettext('Contest with this name already exists!'))
			return jsonify(errors=form.errors), 409
	return "", 406


@contest.route('problem/<string:contest_id>/', methods=['POST'])
def add_problem(contest_id):
	main_form = AddProblem.from_json(request.json)
	#checking  forms validation
	if not (main_form.validate()):
		return "", 406
	
	sub_forms = []
	for sub_form in main_form.data['testcases'] :
		sub_forms.append (sub_form)

	contest_obj = Contest.objects().get(pk = contest_id)
	#checking owner
	if contest_obj.owner.username != logged_in_user():
		return  "", 403

	problem = Problem (title = main_form.data ['title'])
	problem.time_limit = main_form.data ['time_limit']
	problem.space_limit = main_form.data ['space_limit']
	problem.header = main_form.data ['header']
	problem.body = main_form.data ['body']
	problem.footer = main_form.data ['footer']

	testcases = []
	order = 1
	for sub_form in sub_forms:
		testcase = Testcase (input = sub_form ['input'])
		testcase.output = sub_form ['output']
		testcase.order = order
		order = order + 1
		testcases.append (testcase)
	problem.testcases = testcases

	
	contest_obj.problems.append (problem)
	problem.order = len (contest_obj.problems)

	contest_obj.save ()
	return "", 201


