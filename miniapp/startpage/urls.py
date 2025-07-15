from django.urls import path, include
from .views import ToursList, UserProfile, ToursDetail
from . import views

urlpatterns = [
    path('tours/', ToursList.as_view(), name='tours_list'),
    path('profile/<int:pk>', UserProfile.as_view(), name='profile'),
    path('tours/<int:pk>', ToursDetail.as_view(), name='tour_detail'),
    path('check-tour/<int:tour_id>/', views.UserStats.check_tour_ownership, name='check_tour'),


]


