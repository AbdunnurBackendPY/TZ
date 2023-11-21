from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .models import Daily_planner

@login_required
def tasks(request):
    tasks = Daily_planner.objects.filter(user=request.user)
    return render(request,
    'Daily_planner.html',
    {'tasks': tasks})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})




