from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Kategori, Artikel
from django.contrib.auth import logout
from django.shortcuts import redirect

def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect('/')

    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')

def kategori(request):

    data_kategori = Kategori.objects.all()

    context = {
        'kategori': data_kategori
    }

    return render(request, 'kategori.html', context)

def tambah_kategori(request):

    if request.method == 'POST':

        nama = request.POST.get('nama')

        Kategori.objects.create(
            nama=nama
        )

        return redirect('/kategori')

    return render(request, 'tambah_kategori.html')

def edit_kategori(request, id):

    kategori = Kategori.objects.get(id=id)

    if request.method == 'POST':

        kategori.nama = request.POST.get('nama')

        kategori.save()

        return redirect('/kategori')

    context = {
        'kategori': kategori
    }

    return render(request, 'edit_kategori.html', context)

def hapus_kategori(request, id):

    kategori = Kategori.objects.get(id=id)

    kategori.delete()

    return redirect('/kategori')

def artikel(request):

    data_artikel = Artikel.objects.all()

    context = {
        'artikel': data_artikel
    }

    return render(request, 'artikel.html', context)

def tambah_artikel(request):

    kategori = Kategori.objects.all()

    if request.method == 'POST':

        judul = request.POST.get('judul')
        konten = request.POST.get('konten')
        kategori_id = request.POST.get('kategori')
        status = request.POST.get('status')

        Artikel.objects.create(
            judul=judul,
            konten=konten,
            kategori_id=kategori_id,
            status=status
        )

        return redirect('/artikel')

    context = {
        'kategori': kategori
    }

    return render(request, 'tambah_artikel.html', context)

def edit_artikel(request, id):

    artikel = Artikel.objects.get(id=id)

    kategori = Kategori.objects.all()

    if request.method == 'POST':

        artikel.judul = request.POST.get('judul')
        artikel.konten = request.POST.get('konten')
        artikel.kategori_id = request.POST.get('kategori')
        artikel.status = request.POST.get('status')

        artikel.save()

        return redirect('/artikel')

    context = {
        'artikel': artikel,
        'kategori': kategori
    }

    return render(request, 'edit_artikel.html', context)

def hapus_artikel(request, id):

    artikel = Artikel.objects.get(id=id)

    artikel.delete()

    return redirect('/artikel')

def logout_view(request):
    logout(request)
    return redirect('/')