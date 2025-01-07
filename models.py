from django.db import models
from django.urls import reverse


class Home(models.Model):
    name_home = models.CharField(max_length=200,
                                 help_text="Введите название дома",
                                 verbose_name="Название дома")
    description = models.TextField(max_length=1000,
                                   help_text="Введите краткое описание дома",
                                   verbose_name="Описание дома")
    price = models.DecimalField(decimal_places=2, max_digits=7,
                                help_text="Введите цену за сутки",
                                verbose_name="Цена (руб.)")
    photo = models.ImageField(upload_to='images',
                              help_text="Введите изображение дома",
                              verbose_name="Изображение дома")

    def __str__(self):
        return self.name_home

    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])


class Fish(models.Model):
    name_fish = models.CharField(max_length=200,
                                 help_text="Введите название рыбы",
                                 verbose_name="Название рыбы")
    description = models.TextField(max_length=1000,
                                   help_text="Введите краткое рыбы",
                                   verbose_name="Описание рыбы")
    price = models.DecimalField(decimal_places=2, max_digits=7,
                                help_text="Введите цену за килограмм",
                                verbose_name="Цена (руб.)")
    photo = models.ImageField(upload_to='images',
                              help_text="Введите изображение рыбы",
                              verbose_name="Изображение рыбы")

    def __str__(self):
        return self.name_fish

    def get_absolute_url(self):
        return reverse('fish-detail', args=[str(self.id)])
