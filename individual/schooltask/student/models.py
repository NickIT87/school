from django.db import models

# Create your models here.
class Eleventh(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    phone = models.CharField(max_length=17, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['name']
