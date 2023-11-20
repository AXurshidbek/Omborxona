from django.urls import path
from .views import *

urlpatterns = [
path('bolimlar/', BolimlarView.as_view()),
path('mahsulotlar/', MahsulotView.as_view()),

]