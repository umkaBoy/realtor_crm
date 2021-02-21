from django.db import models
from django.contrib.auth.models import User
from crm.consts import LOT_STATUSES, TRIM_TYPES, VIEW_FROM_WINDOWS
from crm.utils.base import images_upload_path
import datetime, os
from django.utils.html import mark_safe



class Lot(models.Model):
    updated_by = models.ForeignKey(User, verbose_name='Кем изменена', on_delete=models.DO_NOTHING, \
                                   blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')

    name = models.CharField(verbose_name='Наименование', blank=False, null=False, max_length=128, default='')
    status = models.CharField(verbose_name='Статус', choices=LOT_STATUSES, blank=False, null=False, max_length=128, default='Свободно')
    # Лот
    n_on_price = models.CharField(verbose_name='№ по прайсу', null=False, blank=True, default='', max_length=64)
    type_object = models.ForeignKey('crm.PremisesType', verbose_name='Тип объекта', null=True, on_delete=models.SET_NULL)
    floor = models.IntegerField(verbose_name='Этаж', blank=True, null=False, default=0)
    s = models.FloatField(verbose_name='Площадь', null=False, blank=False, default=0)
    trim = models.CharField(verbose_name='Отделка', choices=TRIM_TYPES, null=False, blank=False, max_length=32)
    view_from_windows = models.CharField(verbose_name='Вид из окон', null=False, blank=False, choices=VIEW_FROM_WINDOWS, max_length=32)
    options = models.TextField(verbose_name='Опции', null=False, blank=True, default='')
    reward = models.FloatField(verbose_name='Вознаграждение', null=True, blank=True)
    currency = models.CharField(verbose_name='Цена в валюте', null=False, blank=True, default='', max_length=32)
    price = models.FloatField(verbose_name='Цена в руб.', null=False, blank=False, default=0)
    plan = models.ForeignKey('crm.Plan', verbose_name='План помещения', null=True, on_delete=models.DO_NOTHING)
    comment = models.TextField(verbose_name='Комментарий', null=False, blank=True, default='')

    def __str__(self):
        return self.name




class Plan(models.Model):
    name = models.CharField(verbose_name='Название', null=True, blank=False, default='', max_length=64)
    updated_by = models.ForeignKey(User, verbose_name='Кем изменена', on_delete=models.DO_NOTHING, \
                                   blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')
    plan = models.ImageField(upload_to=images_upload_path, null=False, verbose_name='План')
    plan_floor = models.ForeignKey('crm.Floor', verbose_name='Планировка этажа', related_name='floors', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'План помещения'
        verbose_name_plural = 'Планы помещений'

    def __str__(self):
        return self.name or self.id

    @property
    def get_size(self):
        if os.path.exists(self.plan.path):
            return "%0.1f KB" % (os.path.getsize(self.plan.path) / (1024.0))
        return "0 MB"

    get_size.fget.short_description = u'Размер'

    @property
    def get_created_at(self):
        if os.path.exists(self.plan.path):
            statbuf = os.stat(self.plan.path)
            return datetime.datetime.utcfromtimestamp(statbuf.st_ctime).date()
        return ''

    get_created_at.fget.short_description = u'Дата загрузки'

    def image_tag(self):
        if self.plan:
            return mark_safe('<img src="/media/%s" width="350" height="auto" />' % (self.plan))
        return 'Изображение отсутствует'

    image_tag.short_description = 'Image'



class NewBuildingLot(Lot):
    corp = models.ForeignKey('crm.Corp', verbose_name='Корпус', null=False, blank=True, on_delete=models.CASCADE)
    lease = models.CharField(verbose_name='Сдача', null=False, blank=True, default='', max_length=128)
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Новостройка'
        verbose_name_plural = 'Новостройки'



class OldBuildingLot(Lot):
    corp = models.ForeignKey('crm.Corp', verbose_name='Корпус', null=True, blank=True, on_delete=models.CASCADE)
    lease = models.CharField(verbose_name='Сдача', null=False, blank=True, default='', max_length=128)
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вторичка'
        verbose_name_plural = 'Вторички'