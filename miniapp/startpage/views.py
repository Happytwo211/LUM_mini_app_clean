from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import DetailView, ListView
from .forms import PhoneForm, VerificationForm
from .services.sms_service import SMSService
from .models import CustomUser, Tour

class ToursDetail(DetailView):
    model = Tour
    template_name = 'tours_detail.html'
    context_object_name = 'tour'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['tour_elements'] = self.object.tourelements_set.all()
        return contex

class ToursList(ListView):
    model = Tour
    ordering = 'tour_name'
    template_name = 'tours_list.html'
    context_object_name = 'tours'
    paginate_by = 3


def send_verification_code(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']

            try:
                user, created = CustomUser.objects.get_or_create(phone=phone)
                verification_code = user.generate_verification_code()

                # Отправка SMS
                sms_service = SMSService()
                message = f"Ваш код подтверждения: {verification_code}"
                if sms_service.send_sms(phone, message):
                    request.session['phone'] = phone
                    return redirect('verify_code')
                else:
                    messages.error(request, 'Ошибка отправки SMS')
            except Exception as e:
                messages.error(request, 'Произошла ошибка')

    else:
        form = PhoneForm()

    return render(request, 'auth/send_code.html', {'form': form})


def verify_code(request):
    phone = request.session.get('phone')
    if not phone:
        return redirect('send_code')

    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']

            try:
                user = CustomUser.objects.get(phone=phone)
                if user.verification_code == code:
                    user.is_verified = True
                    user.save()

                    # Авторизуем пользователя
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Неверный код')
            except CustomUser.DoesNotExist:
                messages.error(request, 'Пользователь не найден')

    else:
        form = VerificationForm()

    return render(request, 'auth/verify_code.html', {
        'form': form,
        'phone': phone
    })


from django.core.cache import cache


def send_verification_code(request):

    if request.method == 'POST':
        # Проверка лимита запросов
        ip = request.META.get('REMOTE_ADDR')
        key = f'sms_limit_{ip}'
        attempts = cache.get(key, 0)

        if attempts >= 5:
            messages.error(request, 'Слишком много попыток. Попробуйте через час.')
            return render(request, 'auth/send_code.html', {'form': PhoneForm()})

        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']

            try:
                user, created = CustomUser.objects.get_or_create(phone=phone)
                verification_code = user.generate_verification_code()

                # Отправка SMS
                sms_service = SMSService()
                message = f"Ваш код подтверждения: {verification_code}"
                if sms_service.send_sms(phone, message):
                    # Увеличиваем счетчик попыток
                    cache.set(key, attempts + 1, timeout=3600)
                    request.session['phone'] = phone
                    return redirect('verify_code')
                else:
                    messages.error(request, 'Ошибка отправки SMS')
            except Exception as e:
                messages.error(request, 'Произошла ошибка')

    else:
        form = PhoneForm()

    return render(request, 'auth/send_code.html', {'form': form})