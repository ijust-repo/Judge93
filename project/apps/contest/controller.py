# -*- coding: utf-8 -*-
__author__ = ['Kia' , 'SALAR', 'F4RZ4N']


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
from project.utils.Methods_Blacklist import python_methods_blacklist, java_methods_blacklist, cpp_methods_blacklist

#models import
from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest, Problem, Testcase, TeamInfo, Result
#other
import os , zipfile, shutil
from zipfile import BadZipfile
from datetime import datetime
from mongoengine import DoesNotExist, NotUniqueError
from werkzeug.exceptions import RequestEntityTooLarge

import random
import string
import subprocess
import time
import re


@contest.route('contest/', methods=['GET'])
def contest_contest_page():
	return render_template('contest.html')


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


@contest.route('<string:contest_id>/testcase/<int:number>/', methods=['POST'])
def upload_tastecase (contest_id, number):
	data = request.data

	try:
		contest = Contest.objects().get(pk = contest_id)
		contest_name = contest.name
	except DoesNotExist:
		return jsonify(errors="Contest does not exist!"), 406

	max_num = len(contest.problems)
	if number < 1 or number > max_num:
		return jsonify(errors="Invalid problem number!"), 406

	upload_path = "project/contests/" + str (contest_name) + "/testcases/" + str (number) + '/'
	filename = str('testcase ') + str (number)+ ".zip"
	if not os.path.exists(upload_path):
		os.makedirs(upload_path)
	else :
		shutil.rmtree (upload_path)
		os.makedirs(upload_path)
	with open(os.path.join(upload_path, filename), 'wb') as file:
		file.write(data)
	
	try:
		with zipfile.ZipFile(os.path.join(upload_path + filename)) as zf:
			zf.extractall(os.path.join(upload_path))
	except BadZipfile as e:
		shutil.rmtree (upload_path)
		return jsonify(errors="Bad zip file!"), 406
	
	allowed_extensions = ['txt', 'tc']
	unziped_files = os.listdir (upload_path)
	unziped_files.remove (filename)
	os.remove (upload_path + filename)
	for f in  unziped_files:
		if not f.split('.') [-1] in allowed_extensions:
			if os.path.isdir(upload_path + f):
				shutil.rmtree (upload_path + f)
			else:
				os.remove (upload_path + f)

	return "", 200


@contest.route('<string:contest_id>/add_team/<string:team_id>/', methods=['POST'])
def add_team (contest_id,team_id):
  try:
    team_obj = Team.objects().get(pk=team_id)
    contest_obj = Contest.objects().get(pk=contest_id)
    for info in contest_obj.teams:
      if (team_obj == info.team):
        return jsonify(errors = 'team already exists!'), 409

    team_info = TeamInfo (team = team_obj)
    team_info.accepted = False
    team_info.id = len (contest_obj.teams) + 1
    lst = contest_obj.teams
    lst.append(team_info)
    contest_obj.teams = lst
    contest_obj.save()
    return "" , 200
  except DoesNotExist:
    return "" , 406

@contest.route('<string:contest_id>/details/', methods=['GET'])
def contest_details(contest_id):

	def calculate_penalty (problems_list,start_time):
		penalty=0
		solved_problem_counter = 0
		for result in problems_list:
			if result["solved"]:
				penalty += (result["failed_tries"]*20)
				solved_problem_counter += 1
				time_delta = result["solved_on"] - start_time
				time_delta_minutes = int(time_delta.total_seconds()//60)
				penalty += time_delta_minutes
		return penalty , solved_problem_counter

	try:
		contest_obj = Contest.objects().get(id=contest_id)
		start_time = contest_obj.starts_on

		#[details_dict,details_dict,details_dict,...] sort keys (penalty,solved_problem_counter)
		final_list = []

		#keys = team , problems_list, solved_problem_counter , penalty
		details_dict = {}

		#[result_dict,result_dict,result_dict,...] sort key is order
		problems_list = []

		#keys = failed_tries , solved , id , order
		result_dict ={}

		for team_info in contest_obj.teams:
			details_dict["team"] = (team_info.team.to_json())

			for result in team_info.problem_results:
				result_dict["failed_tries"] = (result.failed_tries)
				result_dict["solved"] = (result.solved)
				result_dict["solved_on"] = (result.solved_on)
				result_dict["problem_id"] = (result.problem_id)
				for problem_obj in contest_obj.problems:
					if problem_obj.id == result.problem_id:
						result_dict["order"] = problem_obj.order
						break
				problems_list.append(result_dict)
				result_dict={}
			problems_list.sort(key = lambda resultdictionary :resultdictionary["order"])
			details_dict["problems_list"] = problems_list
			penalty = calculate_penalty(problems_list,start_time)
			details_dict["penalty"] = penalty[0]
			details_dict["solved_problem_counter"] = penalty[1] 
			final_list.append(details_dict)
			details_dict = {}
			problems_list=[]
		final_list.sort(key = lambda detailsdictionary :detailsdictionary["penalty"])
		final_list.sort(key = lambda detailsdictionary :detailsdictionary["solved_problem_counter"] , reverse = True)
		return jsonify(contests = final_list) , 200
	except DoesNotExist:
		return "" , 406

@contest.route('submit/<string:contest_id>/<string:team_id>/<int:number>/<string:file_type>/', methods=['POST'])
def submit (contest_id, team_id ,number, file_type):
	data = request.data

	allowed_filetypes = ['py','cpp','java']
	if( file_type not in allowed_filetypes ):
                Update_Result(contest_id, team_id, number ,"Extension Error", False)
                return "Extension Error", 406
        
	try:
		contest = Contest.objects().get(pk = contest_id)
		contest_name = contest.name
	except DoesNotExist:
		return jsonify(errors="Contest does not exist!"), 406

	try:
		team = Team.objects().get(pk = team_id)
		team_name = team.name
		members_list=[]
		members_list.append(team.owner.username)
		for i in team.members :
			members_list.append(i.username)
                if logged_in_user() not in members_list:
                        return "You Are Not A Member Of This Team", 406
	except DoesNotExist:
		return jsonify(errors="Team does not exist!"), 406

	max_num = len(contest.problems)
	if number < 1 or number > max_num:
		return jsonify(errors="Invalid problem number!"), 406

        # Upload...
	upload_path = "project/contests/" + str (contest_name) + "/testcases/" + str (number) + '/submission_codes/' 
	filename = str('code_') + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15)) + ".%s" %file_type
	if not os.path.exists(upload_path):
		os.makedirs(upload_path)
	with open(os.path.join(upload_path, filename), 'a') as file:
		file.write(data)

        testcases_folder =  "project/contests/" + str (contest_name) + "/testcases/" + str (number) + '/'

        ### Restricted Methods
        is_Restriced = Check_Restricted(upload_path, filename, file_type)
        if is_Restriced:
                Delete_Compile_Files(upload_path, filename, file_type)
                Update_Result(contest_id, team_id, number ,"Restricted Function", False)
                return "Restricted Function", 406
        
        ### Compile...
        if(file_type == "cpp"):
                try:
                        subprocess.check_output("g++ -o %s %s" %(filename[:-4] , os.path.join(upload_path, filename)),shell=True,stderr=subprocess.STDOUT)
                except:
                        Delete_Compile_Files(upload_path, filename, file_type)
                        Update_Result(contest_id, team_id, number ,"Compile Error", False)
                        return "Compile Error", 406
        elif(file_type == "java"):
                try:
                        code_file = open(os.path.join(upload_path, filename), 'r')
                        code = code_file.readlines()
                        for i in range(len(code)):
                                if "public class" in code[i]:
                                        code[i] = code[i].split()
                                        code[i][2] = filename[:-5]
                                        code[i] = ' '.join(code[i])
                                        break
                        code_file.close()
                        code_file = open(os.path.join(upload_path, filename), 'w')
                        code_file.write(" ".join(code))
                        code_file.close()
                        subprocess.check_output("javac %s" %(os.path.join(upload_path, filename)), shell=True,stderr=subprocess.STDOUT)
                except:
                        Delete_Compile_Files(upload_path, filename, file_type)
                        Update_Result(contest_id, team_id, number ,"Compile Error", False)
                        return "Compile Error", 406

        ### Run & Check...
        for testcase in [ i for i in os.listdir(testcases_folder) if i[-2:]=="in" ]:
                if(file_type == "py"):
                        try:
                                out = str(subprocess.check_output("python %s <%s " %(os.path.join(upload_path, filename), os.path.join(testcases_folder, testcase)) ,shell=True,stderr=subprocess.STDOUT))[:-2]
                        except:
                                Delete_Compile_Files(upload_path, filename, file_type)
                                Update_Result(contest_id, team_id, number ,"Runtime Error", False)
                                return "Runtime Error", 406
                elif(file_type == "cpp"):
                        try:
                                out = str(subprocess.check_output("%s.exe <%s " %(filename[:-4], os.path.join(testcases_folder, testcase)),shell=True,stderr=subprocess.STDOUT))
                        except:
                                Delete_Compile_Files(upload_path, filename, file_type)
                                Update_Result(contest_id, team_id, number ,"Runtime Error", False)
                                return "Runtime Error", 406
                elif(file_type == "java"):
                        try:
                                out = str(subprocess.check_output("java -classpath %s %s <%s " %(upload_path, filename[:-5] ,os.path.join(testcases_folder, testcase)),shell=True,stderr=subprocess.STDOUT))[:-2]
                        except:
                                Delete_Compile_Files(upload_path, filename, file_type)
                                Update_Result(contest_id, team_id, number ,"Runtime Error", False)
                                return "Runtime Error", 406
                        

                expected_out_file = open("%s.out" %os.path.join(testcases_folder, testcase[:-3]) , "r")
                expected_out = expected_out_file.read()
                expected_out_file.close()

                #print out, expected_out
                
                if(not expected_out == out):
                        Delete_Compile_Files(upload_path, filename, file_type)
                        Update_Result(contest_id, team_id, number ,"Wrong Answer", False)
                        return "Wrong Answer In TestCase %s" %testcase[:-3], 406
                
        Delete_Compile_Files(upload_path, filename, file_type)
        Update_Result(contest_id, team_id, number ,"Accepted", True)
	return "Accepted", 200

def Delete_Compile_Files(upload_path, filename, file_type):
        try:
                os.remove(os.path.join(upload_path, filename))
                if(file_type == "cpp"):
                        os.remove(filename[:-4] + '.exe')
                if(file_type == "java"):
                        os.remove( os.path.join(upload_path, filename[:-5]) + '.class' )
        except:
                pass
def Check_Restricted(upload_path, filename, file_type):
        uploaded_code_file = open( os.path.join(upload_path, filename) , 'r' )
        uploaded_code = uploaded_code_file.read()
        uploaded_code_file.close()
        blacklist = python_methods_blacklist if file_type == 'py' else cpp_methods_blacklist if file_type == 'cpp' else  java_methods_blacklist

        for i in blacklist:
                regex = re.compile(r"\b%s\b" %i)
                res = bool(regex.search(uploaded_code))
                if (res):
                        return True
        return False

def Update_Result(contest_id, team_id, problem_number ,status, solved):
        contest_obj = Contest.objects().get(pk = contest_id)
        team_obj = Team.objects().get(pk = team_id)

	for complete_team_info in contest_obj.teams:
		if (team_obj == complete_team_info.team):
                        problem_results_list = [ problem_result for problem_result in complete_team_info.problem_results ]
                        if( problem_number not in [ problem_result.problem_id for problem_result in complete_team_info.problem_results ] ):
                                result = Result(problem_id = problem_number)
                                result.status = status
                                result.failed_tries = 1 if (not solved) else 0
                                result.solved = solved
                                if solved:
                                        result.solved_on = datetime.utcnow()
                                problem_results_list.append( result )
                                complete_team_info.problem_results = problem_results_list
                                contest_obj.save()
                                break
                        else:
                                result = [problem_result for problem_result in problem_results_list if( problem_result.problem_id == problem_number )][0]
                                result.status = status
                                result.solved = solved
                                if not solved:
                                        result.failed_tries += 1
                                if solved:
                                        result.solved_on = datetime.utcnow()
                                problem_results_list[problem_results_list.index(result)] = result
                                complete_team_info.problem_results = problem_results_list
                                contest_obj.save()
                                break

