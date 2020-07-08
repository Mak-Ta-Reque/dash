from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def show_cv(request):
    return render(request, 'cv_views.html')


def add_cv(request):
    return render(request, 'add_cv.html')

