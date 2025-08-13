from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tour, TourElements, CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
from .forms import PhoneLoginForm, OTPVerificationForm
from .models import CustomUser
from .utils import send_sms
from .utils import send_sms
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
from .forms import PhoneLoginForm, OTPVerificationForm
from .models import CustomUser
from .utils import send_sms

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


# class UserProfile(DetailView, LoginRequiredMixin):
#     model = UserStats
#     ordering = 'user_stats_to_user'
#     template_name = 'user_profile.html'
#     context_object_name = 'users'


def phone_login(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            user = CustomUser.objects.get(phone=phone)
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()

            # Отправка SMS
            message = f"Ваш код подтверждения: {otp}"
            send_sms(phone, message)

            request.session['phone'] = phone
            return redirect('verify_otp')
    else:
        form = PhoneLoginForm()
    return render(request, 'phone_login.html', {'form': form})


def verify_otp(request):
    phone = request.session.get('phone')
    if not phone:
        return redirect('phone_login')

    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            user = CustomUser.objects.get(phone=phone)

            if user.otp == otp:
                user.is_phone_verified = True
                user.save()
                login(request, user)
                return redirect('home')
            else:
                form.add_error('otp', 'Неверный код')
    else:
        form = OTPVerificationForm()

    return render(request, 'verify_otp.html', {'form': form, 'phone': phone})


@login_required
def home(request):
    return render(request, 'home.html')
