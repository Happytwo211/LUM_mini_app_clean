from django.urls import path, include
from .views import ToursList, ToursDetail
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.phone_login, name='phone_login'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('home/', views.home, name='home'),
]

