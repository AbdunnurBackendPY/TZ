from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from project.users.models import Daily_planner


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class Daily_plannerForm(forms.Form):
    class Meta:
        model = Daily_planner
        field = ['data', 'time', 'description', 'heading']