from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/welcome.html',{'thetime':datetime.now()})

@login_required(login_url='/admin')
def authourized(request):
    return render(request, 'home/authourized.html',{})

