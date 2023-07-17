
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('Stock_Predictor.urls')),
    path("admin/", admin.site.urls),
]
