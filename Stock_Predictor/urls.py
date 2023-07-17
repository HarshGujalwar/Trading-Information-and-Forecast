from django.urls import path
from . import views

urlpatterns = [
    path('',views.Welcome),
    path('ticker',views.User,name='ticker')
]
