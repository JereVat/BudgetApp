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
        net_income = 0
        saving_time = 0
        target_wealth = 0
        beginning_wealth = 0
        target_interest = 0
        return render(request, index, {'result':result, 'netIncome': net_income, 'savingTime': saving_time,
                                       'targetWealth': target_wealth, 'beginningWealth': beginning_wealth,
                                       'targetInterest': target_interest})

    elif request.method == 'POST':
        net_income = request.POST.get('netIncome')
        saving_time = request.POST.get('savingTime')
        target_wealth = request.POST.get('targetWealth')
        beginning_wealth = request.POST.get('beginningWealth')
        target_interest = request.POST.get('targetInterest')
        result = calculate(net_income, saving_time, target_wealth, beginning_wealth, target_interest)
        return render(request, index, {'result': result, 'netIncome': net_income, 'savingTime': saving_time,
                                       'targetWealth': target_wealth, 'beginningWealth': beginning_wealth,
                                       'targetInterest': target_interest})
