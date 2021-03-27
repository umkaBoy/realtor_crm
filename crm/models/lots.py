from django.db import models
from django.contrib.auth.models import User
from crm.consts import LOT_STATUSES, VIEW_FROM_WINDOWS
from crm.utils.base import images_upload_path
import datetime, os
from django.utils.html import mark_safe
from crm import consts



class Lot(models.Model):
    updated_by = models.ForeignKey(User, verbose_name='Кем изменена', on_delete=models.DO_NOTHING, \
                                   blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')

    status = models.CharField(verbose_name='Статус', choices=LOT_STATUSES, blank=False, null=False, max_length=128, default='Свободно')
    # Лот
    n_on_price = models.CharField(verbose_name='№ по прайсу', null=False, blank=True, default='', max_length=64)
    name = models.CharField(verbose_name='Наименование', null=False, blank=True, max_length=252, choices=consts.NAME_TYPE_ROOMS)
    type_object = models.ForeignKey('crm.PremisesType', verbose_name='Тип объекта', null=True, on_delete=models.SET_NULL)
    floor = models.IntegerField(verbose_name='Этаж', blank=True, null=False, default=0)
    s = models.FloatField(verbose_name='Площадь', null=False, blank=False, default=0)
    trim = models.CharField(verbose_name='Отделка', null=False, blank=False, max_length=32)
    view_from_windows = models.CharField(verbose_name='Вид из окон', null=False, blank=False, choices=VIEW_FROM_WINDOWS, max_length=32)
    options = models.TextField(verbose_name='Опции', null=False, blank=True, default='')
    reward = models.FloatField(verbose_name='Вознаграждение', null=True, blank=True)
    currency = models.CharField(verbose_name='Цена в валюте', null=False, blank=True, default='', max_length=32)
    price = models.FloatField(verbose_name='Цена в руб.', null=False, blank=False, default=0)
    plan = models.ForeignKey('crm.Plan', verbose_name='План помещения', null=True, blank=True, default='', on_delete=models.DO_NOTHING)
    comment = models.TextField(verbose_name='Комментарий', null=False, blank=True, default='')


    def __str__(self):
        price = '{:,}'.format(int(self.price)).replace(',', ' ')
        end = ', {0} м² за {1}₽'.format(int(self.s), price)
        if 'вартир' in self.type_object.name or 'партамент' in self.type_object.name:
            return '{0} {1}{2}'.format(self.type_object.name, self.name, end)
        return self.type_object.name + end

    @property
    def url_plan(self):
        if self.plan:
            return self.plan.plan.url
        return ''


    @property
    def price_per_m(self):
        if self.s and self.price:
            try:
                return self.price / self.s
            except:
                pass
        return ''

    @property
    def currency_per_m(self):
        if self.s and self.currency:
            try:
                return self.currency / self.s
            except:
                pass
        return ''



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
    corp = models.ForeignKey('crm.Corp', verbose_name='Корпус', null=True, blank=True, on_delete=models.CASCADE)
    lease = models.CharField(verbose_name='Сдача', null=False, blank=True, default='', max_length=128)
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', null=True, blank=True, on_delete=models.CASCADE, related_name='new_buildings')

    class Meta:
        verbose_name = 'Новостройка'
        verbose_name_plural = 'Новостройки'

    @property
    def type_building(self):
        return 'newbuildinglot'

    @property
    def corp_name(self):
        if self.corp:
            return self.corp.name
        return ''


class OldBuildingLot(Lot):
    corp = models.ForeignKey('crm.Corp', verbose_name='Корпус', null=True, blank=True, on_delete=models.CASCADE)
    lease = models.CharField(verbose_name='Сдача', null=False, blank=True, default='', max_length=128)
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', null=True, blank=True, on_delete=models.CASCADE, related_name='old_buildings')

    class Meta:
        verbose_name = 'Вторичка'
        verbose_name_plural = 'Вторички'


    @property
    def type_building(self):
        return 'oldbuildinglot'

    @property
    def corp_name(self):
        if self.corp:
            return self.corp.name
        return ''
