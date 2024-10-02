 from .models import Daily_planner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django import forms

class EmailRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']




class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user








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
