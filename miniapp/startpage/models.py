from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, request

class Tour(models.Model):

    CONTENT_TYPE = 'Экскурсия'

    tour_content_type = models.CharField(default=CONTENT_TYPE, editable=False)
    tour_time_add = models.TimeField(auto_now=True)
    tour_date_add = models.DateField(auto_now_add=True)

    tour_name = models.CharField(max_length=300, default='Экскурсия')
    tour_desc = models.TextField(max_length=2000, default='Описание экскурсии')
    tour_rating = models.IntegerField(default=10)
    tour_duration = models.IntegerField(default=5)
    tour_value = models.IntegerField(default=500)
    tour_location = models.CharField(max_length=200, default='Location')
    tour_photo = models.ImageField(upload_to='tours/')


    def __str__(self):
        return f'{self.tour_name} : {self.tour_desc}'


class TourElements(models.Model):
    tour_el_to_tour = models.ForeignKey(to=Tour, max_length=50, default='tour_el', on_delete=models.CASCADE)
    tour_element = models.CharField(max_length=50, default='tour_el')
    tour_element_desc = models.CharField(max_length=150, default='tour_el_desc')
    tour_element_img = models.ImageField(upload_to='tour_element_img/', null=True, blank=True)

    def __str__(self):
        return f'{self.tour_el_to_tour}:{self.tour_element}'


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'phone'  # Указываем, что логин по телефону
    REQUIRED_FIELDS = ['username']  # username всё ещё требуется для createsuperuser

    def __str__(self):
        return self.phone



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


