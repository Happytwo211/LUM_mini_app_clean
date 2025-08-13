from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
class PhoneLoginForm(forms.Form):
    phone = forms.CharField(max_length=20)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Пользователь с таким номером не найден")
        return phone

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6)