from django.urls import path
from . import views

urlpatterns = [
    path('', views.jadwal_sholat),
]