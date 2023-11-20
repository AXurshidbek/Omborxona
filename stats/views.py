from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View

class StatsView(View):
    def get(self,request):
        content={
            "foydalanuvchi": request.user.username.capitalize(),
        }
        return render(request, 'stats.html', content)