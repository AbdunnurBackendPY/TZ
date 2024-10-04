from django.urls import path, include
from .models import Daily_planner
from .views import register, tasks, daily_planner
from django.urls import path
from .views import logout_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('TODO/', tasks, name='TODO'),
    path('Daily_planner/', daily_planner, name='daily_planner'),
    path('logout/', logout_view, name='logout'),

]
