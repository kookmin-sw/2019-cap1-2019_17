from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import os
import sys
from pymongo import MongoClient
import json
from django.contrib import messages

connection = MongoClient()
db = connection.summer
summer_collection = db.summer_collection


input_name = {}
save_name = {}
cnt = 1

def index(request):
	#mongoDB
	res = summer_collection.find()
	res_results = []
	for i in res:
		result ={}
		filename = i['filename']
		duration = i['duration']
		uploaded = i['uploaded']
		keyword = i['keyword']
		result['filename'] = filename		
		result['duration'] = duration
		result['uploaded'] = uploaded
		result['keyword'] = keyword
		result['summary_txt'] = 'capstone/summary/' + filename + '_summary.txt'
		result['overall_txt'] = 'capstone/overallview/' + filename + '_overall.txt'
		result['overall_json'] = 'capstone/overallview/' + filename + '_overall.json'
		lines = []
		f = open("capstone/static/capstone/summary/"+filename+"_summary.txt")
		while True:
			line = f.readline()
			if not line: break
			lines.append(line)
		f.close()
		result['summary_view'] = lines
#		print(result['summary_view'])
		data = {}
		line=''
		with open("capstone/static/capstone/overallview/"+filename+"_overall.json") as json_file:
			for line in json_file:
				data = json.loads(line)
		table_data = data['table']
		dict ={}
		script_data =[]
		for i in table_data:
			dict[i['time']] = i['transcript']
		result['dict'] = dict
		res_results.append(result)
		
	global cnt
	html_name = {}
	# file upload
	if request.method == 'POST':
		uploaded_file = request.FILES['file']	
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		print(name)
		
		# flac check
		fn = name
		check = fn[-5:]
		print(check)
		if check != '.flac':
			messages.error(request, 'The extension is not FLAC.')
			context = { 'res_results' : res_results}
			os.system("sh ../error.sh " + name)
			return render(request, 'capstone/index.html', context)
		
		input_name['name'] = name
		html_name['name'] = name
		cnt=2
		print(input_name['name'])
		messages.success(request, 'File Uploaded!')	
	
	# url upload	
	if 'url_input' in request.GET and 'save_name' in request.GET:
		
		#file Name Duplicate Detection
		check = summer_collection.find()
		db_name =[]
		for i in check :
			db_name.append(i['filename'])
		for i in db_name:
			if 	i == request.GET['save_name']:
				print('FileName exists')
				messages.error(request, 'FileName exists')
				context = { 'res_results' : res_results}
				
				return render(request, 'capstone/index.html', context)

				
		input_name['name'] = request.GET['url_input']
		html_name['name'] = request.GET['url_input']
		save_name['name'] = request.GET['save_name']
		messages.success(request, 'URL Uploaded!')
		cnt=3

		
			
	if 'sentence' in request.GET and request.GET['sentence']:
		sentence = request.GET['sentence']
		print(sentence)
		
		#file
		if cnt == 2:
			print(input_name['name'])
			print('file_sh')
			messages.success(request, 'Completed a File Summary!')
			os.system("sh ../file.sh " + input_name['name'] + " " + sentence )
			cnt = 1
			
		#url	
		if cnt == 3:
#			print(input_name['name'])
#			print(save_name['name'])
#			print('url_sh')
			messages.success(request, 'Completed a URL Summary!')
			print('\"' +input_name['name']+'\"' + " " + sentence +" " + save_name['name'])
			os.system("sh ../url.sh " +"\""+ input_name['name'] + "\"" +" " + sentence +" " + save_name['name'])
			cnt = 1
		# url sentence filename(확장자제거) 
	
	context = { 'res_results' : res_results, 'html_name' : html_name}
	return render(request, 'capstone/index.html', context)

