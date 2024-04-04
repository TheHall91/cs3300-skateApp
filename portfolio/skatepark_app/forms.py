from django import forms
from .models import Skatepark

class SkateparkForm(forms.ModelForm):
    class Meta:
        model = Skatepark
        fields = '__all__'