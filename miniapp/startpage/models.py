from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, request

class Tour(models.Model):

    CONTENTYPE = 'Экскурсия'

    tour_content_type = models.CharField(default=CONTENTYPE, editable=False)
    tour_time_add = models.TimeField(auto_now=True)
    tour_date_add = models.DateField(auto_now_add=True)

    tour_name = models.CharField(max_length=300, default='Экскурсия')
    tour_desc = models.TextField(max_length=2000, default='Описание экскурсии')
    tour_rating = models.IntegerField(default=10)
    tour_duration = models.IntegerField(default=5)
    tour_value = models.IntegerField(default=500)
    tour_location = models.CharField(max_length=200, default='Location')
    # tour_photo = models.ImageField(upload_to='images/', default='image')
    tour_photo = models.ImageField(upload_to='tours/')
    def __str__(self):
        return f'{self.tour_name} : {self.tour_desc[:20]}'

class UserStats(models.Model):
    user_own_tours = models.ForeignKey(to=Tour, default=None, on_delete=models.CASCADE, unique=True)
    user_stats_to_user = models.ForeignKey(to=User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user_stats_to_user}:{self.user_own_tours}'

    def check_tour_ownership(request, tour_id ):
        try:
            tour = get_object_or_404(Tour, id=tour_id)
            user_stats  = UserStats.objects.filter(
                user_stats_to_user=request.user,
                user_own_tours=tour
            )
            is_owned = user_stats.exists()

            return JsonResponse({
                'is_tour_owned': is_owned
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


class ContentType(models.Model):
    content_type_tour = 'TOUR'
    content_type_game = 'GAME'
    content_type_quiz = 'QUIZ'

    POSITION = [
        (content_type_tour,'Экскурсия'),
        (content_type_game, 'Игра'),
        (content_type_quiz, 'Квиз')
    ]

    choose = models.CharField(max_length=4, choices=POSITION, null=False)


    def __str__(self):
        return f'{self.choose}'