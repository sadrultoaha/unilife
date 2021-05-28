
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView,TemplateView
from .models import info
# Create your views here.

def index(request):
    lists = info.objects.all().order_by('seq_no')
    params = {'lists': lists}
    return render(request, 'index.html', params)
