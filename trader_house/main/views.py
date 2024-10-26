from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/tavern.html')

def help(request):
    return render(request, 'main/help.html')