from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from datetime import datetime

#from .forms import SummaryForm
 
import os
import sys
#class OverwriteStorage(FileSystemStorage):
#
#    def get_available_name(self, name):
#        if self.exists(name):
#            os.remove(os.path.join(SOME_PATH, name))
#        return name
#fs_name = {}
#time = {}


#class OverwriteStorage(FileSystemStorage):
#    def _save(self, name, content):
#        if self.exists(name):
#            self.delete(name)
#        return super(OverwriteStorage, self)._save(name, content)
#    def get_available_name(self, name):
#        return name
input_name = {}
def index(request):
	cnt = '1'
	if request.method == 'POST':
		uploaded_file = request.FILES['file']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		input_name['name'] = name
		print(input_name['name'])
		
	if 'url_input' in request.GET:
		input_name['name'] = request.GET['url_input']
		cnt = '2'
		print(input_name['name'])

#			sentence = request.GET['sentence']
#			print(file_name)
#			print(sentence)
# file로 넣을 때와 url 입력 구별			
#		os.system("sh ../mk.sh" + " " + name)
		#+ " " + sentence
#		context['url'] = uploaded_file.name
#		os.system("sh ../run.sh")
	
	if 'sentence' in request.GET:
		sentence = request.GET['sentence']
		print(sentence)
		if cnt == '1':
			print(input_name['name'])
			#		os.system("sh ../flac.sh " + input_name['url'] + " " + sentence )
		else:
			print(input_name['name'])
		#		os.system("sh ../url.sh " + input_name['url'] + " " + sentence )
		
	return render(request, 'capstone/index.html', input_name)
#	return render(request, 'capstone/index.html', context)
 
#def summary(request):
#	if request.method == 'POST':
#		
#	return render(request, 'capstone/index.html')

#def list(request):
#	form = SummaryForm()
#	return render(request, 'capstone/list.html', {
#		'form': form
#	})

#def summary(request):
#	
#


#def summary_list(request):
#	return render(request, 'capstone/summary_list.html')
#
#def upload_summary(request):
#	return render(request, 'capstone/upload_summary.html')

