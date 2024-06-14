from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f"用户{username}的密码是{password}")
   
    return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            return HttpResponse(f"用户{username}的密码是{password}")
        else:
            return HttpResponse("密码不匹配")