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
        fields =['title', 'review', 'skatepark', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={
                'size': '40',            # Sets the size of the text box
                'maxlength': '100',      # Sets the maximum length of input
                'class': 'form-control', # Adds a CSS class for additional styling
                'placeholder': 'Enter the title here' # Adds a placeholder
            }),
            'review': forms.Textarea(attrs={
                'rows': 5,               # Sets the number of visible text lines
                'cols': 50,              # Sets the visible width of the text box
                'class': 'form-control', # Adds a CSS class for additional styling
                'placeholder': 'Write your content here'
            }),
        }