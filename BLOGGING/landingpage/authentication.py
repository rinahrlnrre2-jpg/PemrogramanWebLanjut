from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):

    pesan = ""

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            pesan = "Username dan Password wajib diisi"

        else:

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('/home')

            else:
                pesan = "Username atau Password salah"

    context = {
        'pesan': pesan
    }

    return render(request, 'login.html', context)