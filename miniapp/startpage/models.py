from django.db import models
from django.contrib.auth.models import User


class Tour(models.Model):
    tour_name = models.CharField(max_length=300, default='Экскурсия')
    tour_desc = models.TextField(max_length=2000, default='Описание экскурсии')
    tour_rating = models.IntegerField(default=10)
    tour_duration = models.IntegerField(default=5)
    tour_value = models.IntegerField(default=500, max_length=10)
    tour_location = models.CharField(max_length=200, default='Location')
    def __str__(self):
        return f'{self.tour_name} : {self.tour_desc[:20]}'

class UserStats(models.Model):
    user_stats_to_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    user_own_tours = models.ForeignKey(to=Tour, on_delete=models.CASCADE, null=True)
    user_bonus_currency = models.IntegerField(null=True)
    user_promocode = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.user_stats_to_user}'

