from django.urls import path
from .views import ToursList, UserProfile

urlpatterns = [
    path('tours/', ToursList.as_view(), name='tours_list'),
    path('profile/<int:pk>', UserProfile.as_view(), name='profile')
]