from django.urls import path
from .views import *

urlpatterns = [
path('bolimlar/', BolimlarView.as_view()),
path('mahsulotlar/', MahsulotView.as_view()),
path('mijozlar/', ClientsView.as_view()),
path('client_update/<int:son>', ClientEdit.as_view()),
path('mahsulot_update/<int:son>', ProductEdit.as_view()),
]