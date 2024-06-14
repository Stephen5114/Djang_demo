from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f"用户{username}的密码是{password}")
    elif request.method == 'GET':
        print(f'Header information:{request.headers.get('User-Agent')}')
        FORBIDDEN_IP = ['127.0.0.1', '0.0.0.0']
        if request.META.get('REMOTE_ADDR') in FORBIDDEN_IP:
            return HttpResponse('Error Exception')
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