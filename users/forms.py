from .models import Daily_planner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {'username': forms.TextInput(attrs={'type': 'text'}),
                   'password1': forms.TextInput(attrs={'type': 'text'}),
                   'password': forms.TextInput(attrs={'type': 'text'})}


class Daily_plannerForm(forms.ModelForm):
    class Meta:
        model = Daily_planner
        fields = ['data', 'time', 'description', 'heading']

        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'heading': forms.TextInput(attrs={'placeholder': 'Enter heading'}),
        }

        labels = {
            'data': 'Date',
            'time': 'Time',
            'description': 'Description',
            'heading': 'Heading',
        }
