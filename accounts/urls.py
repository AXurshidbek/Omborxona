from django.urls import path
from .views import *

urlpatterns = [
path('clients/', ClientsView.as_view()),
path('logout/', LogoutView.as_view()),
]