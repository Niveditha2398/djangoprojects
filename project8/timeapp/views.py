from django.shortcuts import render
from datetime import datetime
# Create your views here.
def display_time(request):
	server_time=datetime.now()
	data={'time':server_time}
	return render(request=request, template_name='timeapp/display.html',context=data)