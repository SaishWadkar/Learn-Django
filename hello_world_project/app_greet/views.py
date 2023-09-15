from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    dic = {'temp':'SAISH WADKAR !'}
    return render(request,'app_greet/index.html',context=dic)

def index_new(request):
    return HttpResponse("<em> Saish Wadkar </em>")
