from django.shortcuts import render
import os
from django.http import HttpResponse

APP_DIR = os.path.abspath(os.path.dirname(__file__))

def serve(request):
	with open(APP_DIR+"\\"+"statement.txt") as f:
		statement = f.readlines()
	with open(APP_DIR+"\\"+"feedback.txt") as f:
		feedback = f.readlines()
	mapping = {}
	print len(statement), len(feedback)
	for i in range(len(statement)):
		try: mapping[statement[i]] = feedback[i] #less feedback --why?
		except: pass
	r_f = []
	r_s = []
	for key in mapping.keys():
		r_s.append(key)
		r_f.append(mapping[key])
	return render(request, 'ss.html', {'statement': r_s, 'feedback': r_f, 'first': r_s[0]})

def process_submission(request):
	print request.POST, request.GET
	return HttpResponse("")