from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tour, UserStats
class ToursList(ListView):
    model = Tour
    ordering = 'tour_name'
    template_name = 'tours_list.html'
    context_object_name = 'tours'

class UserProfile(DetailView):
    model = UserStats
    ordering = 'user_stats_to_user'
    template_name = 'user_profile.html'
    context_object_name = 'users'
# Create your views here.

