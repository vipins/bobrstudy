from django.shortcuts import render
import os
from django.http import HttpResponse

APP_DIR = os.path.abspath(os.path.dirname(__file__))

def name(request):
	return render(request, 'start.html')

def name_recd(request):
	print request.GET["fullname"]
	return HttpResponseRedirect('/start/')
	
def serve(request):
	with open(APP_DIR+"\\"+"statement.txt") as f:
		statement = f.readlines()
	with open(APP_DIR+"\\"+"feedback.txt") as f:
		feedback = f.readlines()
	with open(APP_DIR+"\\"+"key.txt") as f:
		correct_key = f.readlines()
	mapping = {}
	print len(statement), len(feedback)
	for i in range(len(statement)):
		try: mapping[statement[i]] = [feedback[i], correct_key[i]] #less feedback --why?
		except: pass
	r_s = []
	r_f = []
	r_c = []
	for key in mapping.keys():
		r_s.append(key)
		r_f.append(mapping[key][0])
		r_c.append(mapping[key][1])
	return render(request, 'ss.html', {'statement': r_s, 'feedback': r_f, 'corr_key': r_c, 'first': r_s[0]})

def process_submission(request):
	print request.POST, request.GET
	return HttpResponse("")