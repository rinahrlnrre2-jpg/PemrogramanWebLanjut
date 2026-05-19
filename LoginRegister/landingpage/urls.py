from django.urls import path
from . import views
from .authentication import login_view

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]