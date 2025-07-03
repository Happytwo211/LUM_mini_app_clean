from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tour, UserStats

class ToursDetail(DetailView):
    model = Tour
    template_name = 'tours_detail.html'
    context_object_name = 'tour'

class ToursList(ListView):
    model = Tour
    ordering = 'tour_name'
    template_name = 'tours_list.html'
    context_object_name = 'tours'
    paginate_by = 3

class TourDetail(DetailView):
    model = Tour
    template_name = 'tour_detail.html'
    context_object_name = 'tour'

class UserProfile(DetailView, LoginRequiredMixin):
    model = UserStats
    ordering = 'user_stats_to_user'
    template_name = 'user_profile.html'
    context_object_name = 'users'


class TourDetailTEST(ListView):
    model = Tour
    template_name = 'test_drop_down.html'
    context_object_name = 'tour'