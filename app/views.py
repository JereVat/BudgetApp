from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from templates import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.utils import timezone
from django.core import serializers
import json
import urllib.request
import requests
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def main(request):
    template = 'index.html'

    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            project_filter = "Kaikki projektit - 0"
            return render(request, template)
        else:
            return HttpResponseRedirect('/')