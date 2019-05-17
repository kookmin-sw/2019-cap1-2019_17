from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def index(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['file']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)
#		print(uploaded_file.name)
		
	return render(request, 'capstone/index.html')

