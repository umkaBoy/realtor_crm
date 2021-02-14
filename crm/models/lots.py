from django.db import models
from django.contrib.auth.models import User


class Lot(models.Model):
    updated_by = models.ForeignKey(User, verbose_name='Кем изменена', on_delete=models.DO_NOTHING, \
                                   blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')

    name = models.CharField(verbose_name='Наименование', blank=False, null=False, max_length=128, default='')

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'
        ordering = ['name']

    def __str__(self):
        return self.name