from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def abee(request):
    return HttpResponse('<marquee><h1>bee bee</h1></marquee>')