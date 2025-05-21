from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/login.html', {'error': 'Identifiants invalides'})
    return render(request, 'login/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')