from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os
import sys

input_name = {}
cnt = 1
def index(request):
	global cnt
	html_name = {}
	# file upload
	if request.method == 'POST':
		uploaded_file = request.FILES['file']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		input_name['name'] = name
		html_name['name'] = name
		cnt=2
		print(input_name['name'])
	# url upload	
	if 'url_input' in request.GET:
		input_name['name'] = request.GET['url_input']
		html_name['name'] = request.GET['url_input']
		cnt=3
		print(input_name['name'])

	if 'sentence' in request.GET and request.GET['sentence']:
		sentence = request.GET['sentence']
		print(sentence)
		if cnt == 2:
			print(input_name['name'])
			print('CNT_TWO')
			#		os.system("sh ../flac.sh " + input_name['name'] + " " + sentence )
			cnt = 1
			
		if cnt == 3:
			print(input_name['name'])
			print('CNT_THREE')
		#		os.system("sh ../url.sh " + input_name['name'] + " " + sentence )
			cnt = 1
		
	return render(request, 'capstone/index.html', html_name)

