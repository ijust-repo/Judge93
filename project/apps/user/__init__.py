# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# flask imports
from flask import Blueprint


user = Blueprint('user', __name__,
                 url_prefix='/user/')

from . import controller
