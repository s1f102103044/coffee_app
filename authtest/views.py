from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html', {})

@login_required
def private_page1(request):
    return render(request, 'authtest/private1.html', {})

@login_required
def private_page2(request):
    return render(request, 'authtest/private2.html', {}) 

@login_required
def private_page3(request):
    return render(request, 'authtest/private3.html', {})     

def public_page(request):
    return render(request, 'authtest/public.html', {})