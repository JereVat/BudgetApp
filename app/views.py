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
from app.calculations import calculate

def main(request):
    index = 'index.html'


    if request.method == 'GET':
        result = 0
        return render(request, index, {'result':result})

    elif request.method == 'POST':
        result = calculate(request.POST.get('netIncome'), request.POST.get('savingTime'),
                           request.POST.get('target_wealth'),request.POST.get('beginningWealth'),
                           request.POST.get('targetInterest'))
        return render(request, index, {'result':result})
