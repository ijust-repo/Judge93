# -*- coding: utf-8 -*-
__author__ = ['Kia' , 'SALAR']


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.team import team
from project.apps.contest import contest

from project.apps.contest.forms import CreateContest , AddProblem

from project.apps.contest.forms import CreateContest , AddProblem, EditContest
from project.utils.access import login_user, logout_user, logged_in_user
from project.utils.date import datetime_to_str, str_to_datetime

#models import
from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest, Problem, Testcase
#other
from datetime import datetime
from mongoengine import DoesNotExist, NotUniqueError


@contest.route('/', methods=['POST'])
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


@contest.route('<string:contest_id>/problem/', methods=['POST'])
def add_problem(contest_id):
	main_form = AddProblem.from_json(request.json)
	#checking  forms validation
	if not (main_form.validate()):
		return "", 406
	
	contest_obj = Contest.objects().get(pk = contest_id)
	#checking owner
	if contest_obj.owner.username != logged_in_user():
		return  jsonify(errors="User is not owner!"), 403

	sub_forms = []
	for sub_form in main_form.data['testcases'] :
		sub_forms.append (sub_form)

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
		testcase.id = order
		order = order + 1
		testcases.append (testcase)
	problem.testcases = testcases

	contest_obj.problems.append (problem)
	problem.order = len (contest_obj.problems)
	problem.id = len (contest_obj.problems)
	contest_obj.save ()
	return "", 201


@contest.route('<string:contest_id>/', methods=['PUT'])
def edit(contest_id):
	main_form = EditContest.from_json(request.json)
	#checking  forms validation
	
	if not (main_form.validate()):
		return "", 406
	
	contest_obj = Contest.objects().get(pk = contest_id)
	starts_on = main_form.data['starts_on']
	ends_on = main_form.data['ends_on']
	name = main_form.data['name']
	if starts_on and ends_on:
		if (starts_on > ends_on) :
			main_form.starts_on.errors.append(main_form.starts_on.gettext('Start date must be earlier than end date!'))
			return jsonify(errors=form.errors), 406
		if contest_obj.created_on > datetime.fromtimestamp(starts_on) :
			main_form.starts_on.errors.append(main_form.starts_on.gettext('Start date must be later than creation time!'))
			return jsonify(errors=main_form.errors), 406
	if starts_on and not(ends_on):
		if (datetime.fromtimestamp(starts_on) > contest_obj.ends_on) :
			main_form.starts_on.errors.append(main_form.starts_on.gettext('Start date must be earlier than end date!'))
			return jsonify(errors=main_form.errors), 406
		if contest_obj.created_on > datetime.fromtimestamp(starts_on) :
			main_form.starts_on.errors.append(main_form.starts_on.gettext('Start date must be later than creation time!'))
			return jsonify(errors=main_form.errors), 406
	if not(starts_on) and ends_on:
		if (datetime.fromtimestamp(ends_on) < contest_obj.starts_on) :
			main_form.starts_on.errors.append(main_form.starts_on.gettext('End date must be later than start date!'))
			return jsonify(errors=main_form.errors), 406

	try:
		if name:
			contest_obj.name = name
		if starts_on:
			contest_obj.starts_on = starts_on
		if ends_on:
			contest_obj.ends_on = ends_on
	except NotUniqueError:
		main_form.name.errors.append(main_form.name.gettext('Contest with this name already exists!'))
		return jsonify(errors=main_form.errors), 409

	#checking owner
	if contest_obj.owner.username != logged_in_user():
		return  jsonify(errors="User is not owner!"), 403

	problem_forms = []
	for problem_form in main_form.data['problems'] :
		#problem_forms.append (problem_form)
		for obj in contest_obj.problems:
			if obj.id == problem_form['id']:
				problem = obj
				break
		#alan problem ba id dar omade
		if problem_form['title']:
			problem.title = problem_form['title']
		if problem_form['time_limit']:
			problem.time_limit = problem_form['time_limit']
		if problem_form['space_limit']:
			problem.space_limit = problem_form['space_limit']
		if problem_form['header']:
			problem.header = problem_form['header']
		if problem_form['body']:
			problem.body = problem_form['body']
		if problem_form['footer']:
			problem.footer = problem_form['footer']
		try:
			if problem_form['order']:
				problem.order = problem_form['order']
		except NotUniqueError:
			main_form.problems.errors.append(main_form.problems.gettext('problem order already exists!'))
			return jsonify(errors=main_form.errors), 409
		for testcase_form in problem_form['testcases']:
			for sub_obj in problem.testcases:
				if sub_obj.id == testcase_form['id']:
					case = sub_obj
					break

			if testcase_form['input']:
				print "hi"
				case.input = testcase_form['input'] 
			if testcase_form['output']:
				case.output = testcase_form['output']
			try:
				if testcase_form['order']:
					case.order = testcase_form['order'] 
			except NotUniqueError:
				main_form.problems.errors.append(main_form.problems.gettext('testcase order already exists!'))
				return jsonify(errors=main_form.errors), 409
			if case:
				case.save ()
		problem.save()
	contest_obj.save()
	return "", 200


@contest.route('/', methods=['GET'])
def contests_list():
		create_date_from = request.args.get('create_from', 0.0, type=float)
		create_date_to = request.args.get('create_to', datetime.utcnow(), type=float)
		start_date_from = request.args.get('start_from', 0.0, type=float)
		start_date_to = request.args.get('start_to', datetime.utcnow(), type=float)

		if type(create_date_from) == float:
			create_date_from = datetime.fromtimestamp(create_date_from)

		if type(start_date_from) == float:
			start_date_from = datetime.fromtimestamp(start_date_from)

		if type(create_date_to) == float:
			create_date_to = datetime.fromtimestamp(create_date_to)
			
		if type(start_date_to) == float:
			start_date_to = datetime.fromtimestamp(start_date_to)

		contests_list = []
		print Contest.objects(created_on__gte = create_date_from)
		for obj in (Contest.objects(created_on__gte = create_date_from) and
					Contest.objects(starts_on__gte = start_date_from) and
					Contest.objects(created_on__lte = create_date_to) and
					Contest.objects(starts_on__lte = start_date_to)):

				contests_list.append(obj.to_json())
		return jsonify(contests = contests_list) , 200

@contest.route('by_id/<string:contest_id>/', methods=['GET'])
def contest_info_by_id(contest_id):
	try:
		contest = Contest.objects().get(id=contest_id)
		return jsonify(contest.to_json()) , 200
	except DoesNotExist:
		return "" , 406

@contest.route('by_name/<string:contest_name>/', methods=['GET'])
def contest_info_by_name(contest_name):
	try:
		contest = Contest.objects().get(name=contest_name)
		return jsonify(contest.to_json()) , 200
	except DoesNotExist:
		return "" , 406


@contest.route('details/<string:contest_id>/', methods=['GET'])
def contest_details(contest_id):
	try:
		contest_obj = Contest.objects().get(id=contest_id)
		start_time = contest_obj.starts_on
		current_time = datetime.utcnow()
		#[teams , [problems_list[]] , penalty ]
		#teams = obj.teams[0].team.to_json()
		details_list = []
		#tries = obj.teams[0].problem_results[0].tries
		#solved = obj.teams[0].problem_results[0].solved
		#order = obj.teams[0].problem_results[0].problem.order
		# [order , tries , solved]
		problems_list = []
		for team_info in contest_obj.teams:
			details_list.append(team_info.team.to_json())
			for result in team_info.problem_results:
				problems_list.append(result.problem.order)
				problems_list.append(result.tries)
				problems_list.append(result.solved)
			problems_list.sort(key= lambda order :order[0])
			details_list.append(problems_list)
			print calculate_penalty(problems_list,start_time,current_time)
		return jsonify(contests = details_list) , 200
	except DoesNotExist:
		return "" , 406

def calculate_penalty (problems_list,start_time,current_time):
	penalty=0
	for result in problems_list:
		if result[2]:
			penalty += (result[1]*20)
	time_delta = current_time - start_time
	time_delta_minutes = int(time_delta.total_seconds()//60)
	penalty += time_delta_minutes
	return penalty

@contest.route('add_team/<string:contest_id>/<string:team_name>/', methods=['GET'])
def add_team (contest_id,team_name):
	try:
		team_obj = Team.objects().get(name=team_name)
		contest_obj = Contest.objects().get(pk=contest_id)
		team_info = TeamInfo (team = team_obj)
		team_info.accepted = True
		team_info.id = len (contest_obj.teams)
		print "opwekfwpejf"
		results =[]
		for problem in contest_obj.problems:
			result = Result(problem = problem)
			result.status = ""
			result.tries = 0
			result.solved = True
			result.id = problem.id +27
			print problem.id
			#results.append(result)

		team_info.problem_results = results
		print team_info
		lst = contest_obj.teams
		lst.append(team_info)
		contest_obj.teams = lst
		contest_obj.save()
		return "" , 201
	except Exception, err:
		print err
		return "", 406