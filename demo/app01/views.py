from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hellowordld(request):
    return HttpResponse('hello wordld');

def article_year(request, year):
    return HttpResponse(f"{year}year all article");
