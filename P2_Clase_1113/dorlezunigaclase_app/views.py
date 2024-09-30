from django.shortcuts import render
from django.http import HttpResponse
def hola(request):
    return HttpResponse('HOLA, DORLE, RESPONDIENDO')
# Create your views here.
