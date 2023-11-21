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
        Mahsulot.objects.create(
            nom=request.POST.get("nom"),
            brend=request.POST.get("brend"),
            narx=request.POST.get("narx"),
            miqdor=request.POST.get("miqdor"),
            kelgan_sana=request.POST.get("kelgan_sana"),
            ombor=request.user,
        )

        return redirect("/asosiy/mahsulotlar/")

    def get(self,request):
        content={
            "foydalanuvchi": request.user.username.capitalize(),
            "mahsulotlar": Mahsulot.objects.filter(ombor=request.user),
            "nom": request.user.nom
        }
        return render(request,'products.html',content)


class ClientsView(View):
    def post(self,request):
        Mijoz.objects.create(
            ism=request.POST.get("ism"),
            nom=request.POST.get("nom"),
            manzil=request.POST.get("manzil"),
            tel=request.POST.get("tel"),
            qarz=request.POST.get("qarz"),
            ombor=request.user,
        )
        return redirect("/asosiy/mahsulotlar/")
    def get(self, request):
        content = {
            "mijozlar": Mijoz.objects.filter(ombor=request.user),
            "foydalanuvchi": request.user.username.capitalize(),
            "nom": request.user.nom
        }
        return render(request, 'clients.html', content)

class ClientEdit(View):
    def post(self,request,son):
        Mijoz.objects.filter(id=son).update(
            ism=request.POST.get("ism"),
            nom=request.POST.get("nom"),
            manzil=request.POST.get("manzil"),
            tel=request.POST.get("tel"),
            qarz=request.POST.get("qarz"),
            ombor=request.user,
        )
        return redirect('/asosiy/mijozlar/')
    def get(self,reqest,son):
        content={
            "mijoz": Mijoz.objects.get(id=son),
        }
        return render(reqest, 'client_update.html', content)

class ProductEdit(View):
    def post(self,request,son):
        Mahsulot.objects.filter(id=son).update(
            nom=request.POST.get("nom"),
            brend=request.POST.get("brend"),
            narx=request.POST.get("narx"),
            miqdor=request.POST.get("miqdor"),
            kelgan_sana=request.POST.get("kelgan_sana"),
            ombor=request.user,
        )
        return redirect('/asosiy/mahsulotlar/')
    def get(self,request,son):
        content={
            "mahsulot": Mahsulot.objects.get(id=son)
        }
        return render(request, 'product_update.html', content)