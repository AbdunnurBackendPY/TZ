from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Daily_planner
from .forms import Daily_plannerForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')



def daily_planner(request):
    if request.method == 'POST':
        form = Daily_plannerForm(request.POST)
        if form.is_valid():
            daily_planner = form.save(commit=False)
            daily_planner.user = request.user  # Set the user before saving
            daily_planner.save()
            return redirect("TODO")
    else:
        form = Daily_plannerForm()
    return render(request, 'Daily_planner.html', {'form': form})


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
