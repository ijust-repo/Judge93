# -*- coding: utf-8 -*-
__author__ = "F4RZ4N"


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.team import team
from project.apps.contest import contest

from project.utils.access import logged_in_user
from project.utils.Methods_Blacklist import python_methods_blacklist, java_methods_blacklist, cpp_methods_blacklist

#models import
from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest, Problem, Testcase, TeamInfo, Result
#other
from datetime import datetime
from mongoengine import DoesNotExist, NotUniqueError
import os
import random
import string
import subprocess
import time
import re




@contest.route('submit/<string:contest_id>/<string:team_id>/<int:number>/<string:file_type>/', methods=['POST'])
def submit (contest_id, team_id ,number, file_type):
	data = request.data

	allowed_filetypes = ['py','cpp','java']
	if( file_type not in allowed_filetypes ):
                Update_Result(contest_id, team_id, number ,"Extension Error", False)
                return jsonify(errors="Extension Error"), 406
        
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
                return jsonify(status="Restricted Function"), 200
        
        ### Compile...
        if(file_type == "cpp"):
                try:
                        subprocess.check_output("g++ -o %s %s" %(filename[:-4] , os.path.join(upload_path, filename)),shell=True,stderr=subprocess.STDOUT)
                except:
                        Delete_Compile_Files(upload_path, filename, file_type)
                        Update_Result(contest_id, team_id, number ,"Compile Error", False)
                        return jsonify(status="Compile Error"), 200
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
                        return jsonify(status="Compile Error"), 200

        ### Run & Check...
        for testcase in [ i for i in os.listdir(testcases_folder) if i[-2:]=="in" ]:
                if(file_type == "py"):
                        try:
                                out = str(subprocess.check_output("python %s <%s " %(os.path.join(upload_path, filename), os.path.join(testcases_folder, testcase)) ,shell=True,stderr=subprocess.STDOUT))[:-2]
                        except:
                                Delete_Compile_Files(upload_path, filename, file_type)
                                Update_Result(contest_id, team_id, number ,"Runtime Error", False)
                                return jsonify(status="Runtime Error"), 200
                elif(file_type == "cpp"):
                        try:
                                out = str(subprocess.check_output("%s.exe <%s " %(filename[:-4], os.path.join(testcases_folder, testcase)),shell=True,stderr=subprocess.STDOUT))
                        except:
                                Delete_Compile_Files(upload_path, filename, file_type)
                                Update_Result(contest_id, team_id, number ,"Runtime Error", False)
                                return jsonify(status="Runtime Error"), 200
                elif(file_type == "java"):
                        try:
                                out = str(subprocess.check_output("java -classpath %s %s <%s " %(upload_path, filename[:-5] ,os.path.join(testcases_folder, testcase)),shell=True,stderr=subprocess.STDOUT))[:-2]
                        except:
                                Delete_Compile_Files(upload_path, filename, file_type)
                                Update_Result(contest_id, team_id, number ,"Runtime Error", False)
                                return jsonify(status="Runtime Error"), 200
                        

                expected_out_file = open("%s.out" %os.path.join(testcases_folder, testcase[:-3]) , "r")
                expected_out = expected_out_file.read()
                expected_out_file.close()

                #print out, expected_out
                
                if(not expected_out == out):
                        Delete_Compile_Files(upload_path, filename, file_type)
                        Update_Result(contest_id, team_id, number ,"Wrong Answer", False)
                        return jsonify(status="Wrong Answer In TestCase %s" %testcase[:-3]), 200
                
        Delete_Compile_Files(upload_path, filename, file_type)
        Update_Result(contest_id, team_id, number ,"Accepted", True)
        return jsonify(status="Accepted"), 200

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

