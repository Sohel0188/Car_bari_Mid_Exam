from django import forms
from .models import Car, Comment, BuyCar


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

class BuyCarForm(forms.ModelForm):
    class Meta:
        model = BuyCar
        fields = ['car']       
        
