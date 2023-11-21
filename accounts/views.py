from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View


class LoginView(View):

    def get(self,request):
        return render(request, 'home.html')
    def post(self,request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/asosiy/bolimlar/')
        return redirect('/')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')

