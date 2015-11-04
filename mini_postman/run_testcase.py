#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'AminHP'

import requests as rq
import json
import sys


def send_request(info, headers):
	if info['method'] == 'POST':
		return rq.post(info['url'], data=info['request'], headers=headers)
	elif info['method'] == 'PUT':
		rq.put(info['url'], data=info['request'], headers=headers)
	elif info['method'] == 'GET':
		return rq.get(info['url'], headers=headers)
	elif info['method'] == 'PATCH':
		return rq.patch(info['url'], headers=headers)
	elif info['method'] == 'DELETE':
		return rq.delete(info['url'], headers=headers)

def print_response(resp):
	print "StatusCode: %s\nResponse: %s\n%s\n" % (resp.status_code, resp.text, '-' * 100), 


def run_testcase():
	base_url = 'http://127.0.0.1:5000'
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

	with open('testcase.txt', 'r') as testcase:
		reqs = testcase.read().split('-' * 200)

		for r in reqs:
			name_index = r.find("Name: ")
			method_index = r.find("Method: ")
			url_index = r.find("Url: ")
			request_index = r.find("Request: ")

			if name_index == -1 or method_index == -1 or url_index == -1 or request_index == -1:
				break

			info = {}
			info['name'] = r[name_index + 6: method_index - 1]
			info['method'] = r[method_index + 8: url_index - 1]
			info['url'] = base_url + r[url_index + 5: request_index - 1]
			info['request'] = r[request_index + 9: -2]

			response = send_request(info, headers)
			print_response(response)

if __name__ == '__main__':
	run_testcase()
