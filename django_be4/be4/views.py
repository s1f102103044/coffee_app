from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def root(request):
  params = {}
  params['title'] = 'ただのタイトル'
  #return HttpResponse('Hello Django')
  return render(request, 'be4/index.html', params)