from django.contrib.auth.models import User
from django.db import models
from django.forms.models import modelform_factory
from django import forms



class UserFly(User):
    @staticmethod
    def create(username, email, password):
        user = User.objects.create_user(username, email, password)
        UserExtra.objects.create(user=user)
        return user

    @staticmethod
    def transform(user):
        return UserFly.objects.get(username=user.username)

    def set_photo(self, str):
        self.UserExtra.avatar = str
        self.UserExtra.save()

    def set_info(self, str):
        us = UserExtra.objects.get(user=self)
        us.passport = str;
        us.save()

    def get_info(self):
        return UserExtra.objects.get(user=self).passport

    class Meta:
        proxy = True


class   UserExtra(models.Model):
    passport = models.TextField("Данные удостоверения", max_length=1000, blank=True)
    avatar = models.ImageField(blank=True)
    user = models.OneToOneField(UserFly, on_delete=models.CASCADE)


class   Flight(models.Model):
    class Meta():
        db_table = "fights"
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"
    dep_time = models.DateTimeField("Время вылета")
    arr_time = models.DateTimeField("Время пибытия")
    dep_point = models.CharField("Место отправления", max_length=50)
    arr_point = models.CharField("Место прибытия", max_length=50)


class   Ticket(models.Model):
    class Meta():
        db_table = "tickets"
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"
    cost = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)


class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'user_media/', blank=True)


FormImg = modelform_factory(ExampleModel, fields=("model_pic",))
