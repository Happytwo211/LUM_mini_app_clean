from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tour, UserStats, TourElements

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


class UserProfile(DetailView, LoginRequiredMixin):
    model = UserStats
    ordering = 'user_stats_to_user'
    template_name = 'user_profile.html'
    context_object_name = 'users'


