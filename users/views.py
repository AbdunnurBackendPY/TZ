from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Daily_planner
from .forms import Daily_plannerForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')


def daily_planner(request):
    if request.method == 'POST':
        form = Daily_plannerForm(request.POST)
        if form.is_valid():
            daily_planner = form.save(commit=False)
            daily_planner.user = request.user
            daily_planner.save()
            return redirect("TODO")
    else:
        form = Daily_plannerForm()
    return render(request, 'Daily_planner.html', {'form': form})


@login_required
def tasks(request):
    tasks = Daily_planner.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'delete_task' in request.POST:
            task_id = request.POST.get('delete_task')
            task = get_object_or_404(Daily_planner, pk=task_id, user=request.user)
            task.delete()
            return redirect('TODO')

        if 'save_tasks' in request.POST:
            completed_ids = request.POST.getlist('completed_tasks')
            for task in tasks:
                task.completed = str(task.pk) in completed_ids
                task.save()
            return redirect('TODO')

    return render(request, 'TODO.html', {'tasks': tasks})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
