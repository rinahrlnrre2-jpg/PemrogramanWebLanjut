from django.urls import path
from . import views
from .authentication import login_view

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),

    path('kategori/', views.kategori, name='kategori'),
    path('tambah-kategori/', views.tambah_kategori, name='tambah_kategori'),
    path('edit-kategori/<int:id>', views.edit_kategori, name='edit_kategori'),
    path('hapus-kategori/<int:id>', views.hapus_kategori, name='hapus_kategori'),
    
    path('artikel/', views.artikel, name='artikel'),
    path('tambah-artikel/', views.tambah_artikel, name='tambah_artikel'),
    path('edit-artikel/<int:id>', views.edit_artikel, name='edit_artikel'),
    path('hapus-artikel/<int:id>', views.hapus_artikel, name='hapus_artikel'),

    path('logout/', views.logout_view),
]