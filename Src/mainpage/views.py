from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from mainpage.models import PageModule

# Create your views here.
def mainpage(request):
	pageModule_text_list = PageModule.objects.all()
	context = {'pageModule_text_list' : pageModule_text_list,} 

	return render(request, 'mainpage/index.html', context)