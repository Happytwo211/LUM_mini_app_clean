from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class PhoneForm(forms.Form):
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': '+79123456789',
            'class': 'form-control'
        })
    )

class VerificationForm(forms.Form):
    code = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': '1234',
            'class': 'form-control'
        })
    )