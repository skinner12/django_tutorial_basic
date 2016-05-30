from django.shortcuts import render
from django.http import HttpResponse


def index(responde):
    return HttpResponse('<h2>HeY!!</h2>')
