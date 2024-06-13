from django import forms
from .models import Skatepark, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SkateparkForm(forms.ModelForm):
    class Meta:
        model = Skatepark
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'