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


from django import forms
from .models import Daily_planner

class Daily_plannerForm(forms.ModelForm):
    class Meta:
        model = Daily_planner
        fields = ['data', 'time', 'description', 'heading']

        widgets = {
            'data': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select a date',
                'autocomplete': 'off'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Select time',
                'autocomplete': 'off'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter task description',
                'autocomplete': 'off'
            }),
            'heading': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter heading',
                'autocomplete': 'off'
            }),
        }