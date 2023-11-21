from django.urls import path, include
from .views import register, tasks

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('TODO/', tasks)

]