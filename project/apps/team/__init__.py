# -*- coding: utf-8 -*-
__author__ = 'AminHP'

# flask imports
from flask import Blueprint


team = Blueprint('team', __name__,
                 url_prefix='/team/')

from . import controller
