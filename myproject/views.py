from django.shortcuts import render
from django.http import HttpResponse
import os
def members(request):
    return HttpResponse("Test: Hello world!")
def l1(request):
    return render(request,'index.html')