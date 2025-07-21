from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class PhoneLoginForm(forms.Form):
    phone = forms.CharField(max_length=20)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        try:
            user, created = CustomUser.objects.get_or_create(
                phone=phone,
                defaults={'username': phone}
            )
            return phone
        except Exception as e:
            er_str = f'Произошла ошибка {e}'
            return er_str
        # if not CustomUser.objects.filter(phone=phone).exists():
        #     raise forms.ValidationError("Пользователь с таким номером не найден")
        # return phone

    # def phone_login(request):
    #     if request.method == 'POST':
    #         form = PhoneLoginForm(request.POST)
    #         if form.is_valid():
    #             phone = form.cleaned_data['phone']
    #             # Получаем или создаём пользователя
    #             user, created = CustomUser.objects.get_or_create(phone=phone)
    #             # ... отправка SMS и остальной код

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6)