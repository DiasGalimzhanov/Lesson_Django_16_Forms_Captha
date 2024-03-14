from django import forms
from .models import Lego, Figure
from captcha.fields import CaptchaField

class LegoForm(forms.ModelForm):
    class Meta:
        model = Lego
        fields = ['name', 'size']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название','style': 'width: 30rem;'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Размер','style': 'width: 30rem;'}),
        }

class FigureForm(forms.ModelForm):
    class Meta:
        model = Figure
        fields = ['name', 'lego']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название','style': 'width: 30rem;'}),
            'lego': forms.Select(attrs={'class': 'form-control', 'style': 'width: 30rem;'}),
        }

class LegoFormCaptcha(forms.ModelForm):
    captcha = CaptchaField(generator = 'captcha.helpers.math_challenge')
    class Meta:
        model = Lego
        fields = ['name', 'size']
        labels = {'name': '', 'size': '', 'captcha': ''}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название','style': 'width: 30rem;'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Размер','style': 'width: 30rem;'}),
            #'captcha': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Каптча','style': 'width: 30rem;'}),
        }

class SearchForm(forms.Form):
    name = forms.CharField(max_length=100)
    captcha = CaptchaField(generator = 'captcha.helpers.math_challenge')
