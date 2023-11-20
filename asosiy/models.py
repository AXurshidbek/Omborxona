from django.db import models

from accounts.models import Ombor

class Mahsulot(models.Model):
    nom = models.CharField(max_length=55)
    brend=models.CharField(max_length=25)
    narx=models.PositiveIntegerField()
    miqdor=models.PositiveIntegerField()
    kelgan_sana=models.DateField()
    ombor=models.ForeignKey(Ombor,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Mijoz(models.Model):
    ism=models.CharField(max_length=31)
    nom=models.CharField(max_length=35)
    manzil=models.CharField(max_length=55)
    tel=models.CharField(max_length=21)
    ombor=models.ForeignKey(Ombor, on_delete=models.CASCADE)
    qarz=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.ism} --> {self.nom}'
