from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return render(request, 'models/home.html', locals())

def redirect_home(request):
    return redirect('home')
