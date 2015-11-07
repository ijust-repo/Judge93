# -*- coding: utf-8 -*-
__author__ = ['Kia' , 'SALAR']


#flask import
from flask import jsonify, request, render_template

#project import
from project.apps.user import user
from project.apps.team import team
from project.apps.contest import contest
from project.apps.contest.forms import CreateContest
from project.utils.access import login_user, logout_user, logged_in_user
from project.utils.date import datetime_to_str, str_to_datetime
#models import
from project.apps.user.models import User
from project.apps.team.models import Team
from project.apps.contest.models import Contest
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
