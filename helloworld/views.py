from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from os import listdir



def index(request):
  return render(request, 'home.html')

photo_count=[i+1 for i in range(4)]
def photography(request):
  return render(request, 'photography.html',{'photo_count': photo_count})