# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# flask imports
from flask import Blueprint


user = Blueprint('contest', __name__,
                 url_prefix='/contest/')

from . import controller
