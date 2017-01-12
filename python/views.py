import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
from django.utils.encoding import smart_str

def index(request):    
    return render(request, 'index.html')

def nmap(request) :
    return render(request, 'nmap.py')

def speedtest(request) :
    return render(request, 'speedtest.py')

def main(request) :
    return render(request, 'main.py')

def pingcheck(request) :
    return render(request, 'pingcheck.py')

def webstatus(request) :
    return render(request, 'webstatus.py')

def dependencies(request) :
    return render(request, 'dependencies.py')

def interfaces(request) :
    return render(request, 'interfaces.py')


def download(request) :
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_to_file = os.path.join(BASE_DIR, 'python/download/Python-Scripts-SYSAdmin.zip')
    zip_file = open(path_to_file, 'r')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'Python-Scripts-SYSAdmin.zip'
    return response

