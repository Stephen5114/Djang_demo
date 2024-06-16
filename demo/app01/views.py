
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

def list(request):
    author = 'andy'
    article_number = 20
    article_list = [
        '第一篇文章:什么是Django',
        '第二篇文章: Django的mvt模式',
        '第三篇文章: Django的视图'
    ]
    info = {
        'name': 'andy',
        'age': 18,
        'programming_language': ['python','java', 'c']
    }
    return render(request, 'list.html',{
        'author': author,
        'number': article_number,
        'article_list': article_list,
        'info': info
    })
    
