from django.urls import path
from .views import home, detail, tambah, edit, hapus, register

urlpatterns = [
    path('', home),
    path('detail/<int:id>/', detail),
    path('tambah/', tambah),
    path('edit/<int:id>/', edit),
    path('hapus/<int:id>/', hapus),
    path('register/', register),
]