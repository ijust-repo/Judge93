__author__ = 'AminHP'

# python imports
from datetime import datetime


def datetime_to_str(dt):
	return dt.strftime('%Y-%m-%d %H:%M:%S')


def str_to_datetime(str_dt):
	date, time = str_dt.split(' ')
	year, month, day = date.split('-')
	hour, minutes, seconds = time.split(':')
	return datetime(int(year), 
					int(month), 
					int(day), 
					int(hour), 
					int(minutes), 
					int(seconds))
