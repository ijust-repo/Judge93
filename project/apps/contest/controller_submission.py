# -*- coding: utf-8 -*-
__author__ = "F4RZ4N"


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.team import team
from project.apps.contest import contest
from project.tasks import code_stuff

from project.utils.access import logged_in_user
from project.utils.Methods_Blacklist import python_methods_blacklist, java_methods_blacklist, cpp_methods_blacklist
from project.utils.os_funcs import get_os

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
from signal import SIGTERM
import shutil



@contest.route('submit/<string:contest_id>/<string:team_id>/<int:number>/<string:file_type>/', methods=['POST'])
def submit (contest_id, team_id ,number, file_type):
        data = request.data

        allowed_filetypes = ['py','cpp','java']
        if( file_type not in allowed_filetypes ):
                Update_Result(contest_id, team_id, number ,"Extension Error", False)
                return jsonify(errors="Extension Error"), 406

        try:
                team = Team.objects().get(pk = team_id)
                team_name = team.name
                members_list=[]
                members_list.append(team.owner.username)
                for i in team.members :
                        members_list.append(i.username)
                if logged_in_user() not in members_list:
                        return jsonify(errors="You Are Not A Member Of This Team"), 406
        except DoesNotExist:
                return jsonify(errors="Team does not exist!"), 406

        try:
                is_team_in_contest = False
                contest = Contest.objects().get(pk = contest_id)
                contest_name = contest.name
                for t in contest.teams:
                        if(team == t.team):
                                is_team_in_contest = True
                                if( t.accepted != True ):
                                        return jsonify(errors="You are not allowed to submit"), 406
                                break
                if not is_team_in_contest:
                        return jsonify(errors="You are not allowed to submit"), 406
        except DoesNotExist:
                return jsonify(errors="Contest does not exist!"), 406

        max_num = len(contest.problems)
        if number < 1 or number > max_num:
                return jsonify(errors="Invalid problem number!"), 406

        if datetime.utcnow() < contest.starts_on:
                return jsonify(errors="Contest Is Not Started Yet!"), 406
        elif datetime.utcnow() > contest.ends_on:
                return jsonify(errors="Contest Is Finished!"), 406

        Update_Result(contest_id, team_id, number ,"Pending", False, True)
        code_stuff.apply_async(args=[contest_name, number, file_type, team_name, data, contest_id, team_id])
        return jsonify(status="Pending"), 200



def Update_Result(contest_id, team_id, problem_number ,status, solved, pending = False):
        contest_obj = Contest.objects().get(pk = contest_id)
        team_obj = Team.objects().get(pk = team_id)

        for complete_team_info in contest_obj.teams:
                if (team_obj == complete_team_info.team):
                        problem_results_list = [ problem_result for problem_result in complete_team_info.problem_results ]
                        if( problem_number not in [ problem_result.problem_id for problem_result in complete_team_info.problem_results ] ):
                                result = Result(problem_id = problem_number)
                                result.status = status
                                result.failed_tries = 1 if (not solved and not pending) else 0
                                result.solved = solved
                                if solved:
                                        result.solved_on = datetime.utcnow()
                                problem_results_list.append( result )
                                complete_team_info.problem_results = problem_results_list
                                contest_obj.save()
                                break
                        else:
                                result = [problem_result for problem_result in problem_results_list if( problem_result.problem_id == problem_number )][0]
                                if not result.solved:
                                        result.status = status
                                        result.solved = solved
                                        if not solved and not pending:
                                                result.failed_tries += 1
                                        if solved:
                                                result.solved_on = datetime.utcnow()
                                        problem_results_list[problem_results_list.index(result)] = result
                                        complete_team_info.problem_results = problem_results_list
                                        contest_obj.save()
                                break
