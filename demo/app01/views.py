
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hellowordld(request):
    return HttpResponse('hello wordld');

def article_year(request, year):
    return HttpResponse(f"{year}year all article");

def article_flag(request, year, month, flag):
    return HttpResponse(f"{year}年{month}月的{flag}");

def get_current_datetime(request):
    today = datetime.today()
    format_today = today.strftime("%y-%m-%d")
    html = f"<h1>今天是{format_today}</h1>"
    return HttpResponse(html)
    
