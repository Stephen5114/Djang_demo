from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f"用户{username}的密码是{password}")
    return render(request, 'login.html')