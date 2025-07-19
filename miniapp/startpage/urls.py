from django.urls import path, include
from .views import ToursList, ToursDetail
from . import views

urlpatterns = [
    path('tours/', ToursList.as_view(), name='tours_list'),
    # path('profile/<int:pk>', UserProfile.as_view(), name='profile'),
    path('tours/<int:pk>', ToursDetail.as_view(), name='tour_detail'),
    # path('check-tour/<int:tour_id>/', views.UserStats.check_tour_ownership, name='check_tour'),
    path('login/', views.phone_login, name='phone_login'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('home/', views.home, name='home'),


]


