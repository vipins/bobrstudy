from django.shortcuts import render
import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))

def serve(request):
	with open(APP_DIR+"\\"+"statement.txt") as f:
		statement = f.readlines()
	with open(APP_DIR+"\\"+"feedback.txt") as f:
		feedback = f.readlines()
	return render(request, 'ss.html', {'statement': statement, 'feedback': feedback})