from django.db import models
from django.contrib.auth.models import User


class Developer(models.Model):
    updated_by = models.ForeignKey(User, verbose_name='Кем изменена', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')
    name = models.CharField(verbose_name='Наименование', unique=True, blank=False, null=False, max_length=128, default='')
    created_at = models.CharField(null=False, default='', blank=True, verbose_name='Дата основания', max_length=64)
    description = models.TextField(verbose_name='Описание', blank=True, null=False, default='', max_length=2048)
    objects_delivered = models.IntegerField(verbose_name='Сдано объектов', blank=False, null=True)
    objects_under_construction = models.IntegerField(verbose_name='Объектов строится', blank=False, null=True)


    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'
        ordering = ['name']


    def __str__(self):
        return self.name


    @property
    def count_complexes(self):
        return self.complexes.all().count()
