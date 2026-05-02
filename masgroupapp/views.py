from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Admission

def v1(request):
    return render(request, "v1.html",)

def v1about(request):
    context ={ }
    return render(request, "v1about.html",context=context)

def v1form(request):
    context ={ }
    return render(request, "v1form.html",context=context)

def v1aca(request):
    context ={ }
    return render(request, "v1academics.html",context=context)

def v1fees(request):
    context ={ }
    return render(request, "v1fees.html",context=context)