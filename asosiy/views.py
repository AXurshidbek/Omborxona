from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.views import View



class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        return render(request, '/')
    # def post(self,request):
    #     pass
class MahsulotView(View):

    def post(self,request):
        if request.method == 'POST':
            Mahsulot.objects.create(
                nom=request.POST.get("nom"),
                brend=request.POST.get("brend"),
                narx=request.POST.get("narx"),
                miqdor=request.POST.get("miqdor")
            ).save()
            return redirect("/asosiy/mahsulotlar/")
        content = {
            "muahsulotlar": Mahsulot.objects.all(),
        }
        return render(request, "/asosiy/mahsulotlar/", content)
    def get(self,request):
        conetnt={
            "foydalanuvchi": request.user.username.capitalize(),
        }
        return render(request,'products.html',conetnt)

