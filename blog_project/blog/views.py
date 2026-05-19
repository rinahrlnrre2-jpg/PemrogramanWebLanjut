from django.shortcuts import render, redirect, get_object_or_404
from .models import ArtikelBlog, Kategori
from django.contrib.auth.models import User


def home(request):
    data_artikel = ArtikelBlog.objects.all()
    return render(request, 'home.html', {'artikel': data_artikel})


def detail(request, id):
    artikel = get_object_or_404(ArtikelBlog, id=id)
    return render(request, 'detail.html', {'artikel': artikel})


def tambah(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.method == 'POST':
        ArtikelBlog.objects.create(
            judul=request.POST.get('judul'),
            isi=request.POST.get('isi'),
            kategori_id=request.POST.get('kategori'),
            created_by=request.user
        )
        return redirect('/')

    kategori = Kategori.objects.all()
    return render(request, 'tambah.html', {'kategori': kategori})


def edit(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')

    artikel = get_object_or_404(ArtikelBlog, id=id)

    if request.method == 'POST':
        artikel.judul = request.POST.get('judul')
        artikel.isi = request.POST.get('isi')
        artikel.kategori_id = request.POST.get('kategori')
        artikel.save()
        return redirect('/')

    kategori = Kategori.objects.all()
    return render(request, 'edit.html', {
        'artikel': artikel,
        'kategori': kategori
    })


def hapus(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')

    artikel = get_object_or_404(ArtikelBlog, id=id)
    artikel.delete()
    return redirect('/')


def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        return redirect('/login/')

    return render(request, 'register.html')