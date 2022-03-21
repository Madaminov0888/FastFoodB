
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class BotUser(models.Model):
    chat_id = models.IntegerField(unique=True, auto_created=True, null=True, blank=True)
    full_name = models.CharField(max_length=255, auto_created=True, null=True, blank=True)
    savat = []



class Foods(models.Model):
    class Type(models.TextChoices):
        LAVASH = 'Lavash'
        CHIZBURGER = 'Chizburger'
        PIZZA = 'Pizza'
        PIDE = 'TurkchaPitsa'
        HOTDOG = 'Hotdog'
        DONER = 'Doner'
        ICHIMLIKLAR = 'Ichimliklar'
        KEBAB = 'Kavob'
        FRIE = 'Frie'
    
    class size(models.TextChoices):
        big = 'Katta'
        middle = "O'rtacha"
        little = 'Kichik'
        special = 'Maxsus'

    title = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, default='Ruscha')
    type = models.CharField(max_length=15, choices=Type.choices)
    sum = models.PositiveIntegerField(verbose_name='Narxi')
    description = models.TextField(max_length=225, null=True, default='', verbose_name='Izoh')
    description_ru = models.TextField(max_length=225, null=True, default='', verbose_name='Izoh')
    Size = models.CharField(max_length=15, choices=size.choices, default='')
    #file = models.FileField(null=True, default=0)

    def __str__(self) -> str:
        return str(self.title)

    def get_list_of_all(self):
        return [str(self.title), str(self.type), self.description, self.sum, self.Size]


class Boshagurung(models.Model):
    title = models.CharField(max_length=255)
    gurring = models.TextField(max_length=225, null=True, default='', verbose_name='Izoh')

