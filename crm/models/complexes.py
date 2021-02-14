from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from crm.utils.base import images_upload_path
from crm.consts import TRIM_TYPES


class Complex(models.Model):
    updated_by = models.ForeignKey(User, verbose_name='Кем изменена', on_delete=models.DO_NOTHING, \
                                      blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')

    name = models.CharField(verbose_name='Название', blank=True, null=False, max_length=128, default='')
    region = models.ForeignKey('crm.Region', verbose_name='Регион', null=True, on_delete=models.SET_NULL)
    address = models.TextField(max_length=256, verbose_name='Адрес', null=False, blank=False, default='')
    developer = models.ForeignKey('crm.Developer', verbose_name='Застройщик', null=True, \
                                  on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', blank=False, null=False, default='', max_length=2048)
    start_of_construction = models.DateField(blank=False, null=True, verbose_name='Начало строительства')
    end_of_construction = models.DateField(blank=False, null=True, verbose_name='Сдача')
    construction_tech = models.ForeignKey('crm.ConstructionTech', verbose_name='Технология строительства', null=True, \
                                  on_delete=models.SET_NULL)
    premises_type = models.ForeignKey('crm.PremisesType', verbose_name='Тип помещения', null=True, \
                                  on_delete=models.SET_NULL)
    object_class = models.ForeignKey('crm.ObjectClass', verbose_name='Класс объекта', null=True, \
                                  on_delete=models.SET_NULL)
    count_lots = models.IntegerField(verbose_name='Количество лотов', blank=False, null=True)
    count_floors = models.IntegerField(verbose_name='Этажность', blank=True, null=True)
    infrastructure = models.TextField(verbose_name='Инфраструктура', blank=True, null=False, default='', max_length=2048)
    transport_accessibility = models.TextField(verbose_name='Транспортная доступность', blank=True, null=False, default='', max_length=2048)
    # детали
    trim = models.CharField(verbose_name='Отделка', blank=True, null=False, max_length=128, choices=TRIM_TYPES)
    facade = models.CharField(verbose_name='Фасад', blank=True, null=False, max_length=128, default='')
    elevators = models.CharField(verbose_name='Лифты', blank=True, null=False, max_length=128, default='')
    windows = models.CharField(verbose_name='Окна', blank=True, null=False, max_length=128, default='')
    ventilation = models.CharField(verbose_name='Вентиляция', blank=True, null=False, max_length=128, default='')
    conditioning = models.CharField(verbose_name='Кондиционирование', blank=True, null=False, max_length=128, default='')\
    # Юр. Детали
    cadastre = models.CharField(verbose_name='Кадастр', blank=True, null=False, max_length=128, default='')
    tax = models.CharField(verbose_name='Налог', blank=True, null=False, max_length=64, default='')
    content = models.TextField(verbose_name='Содержание', blank=True, null=False, max_length=512, default='')
    contract = models.CharField(verbose_name='Договор', blank=True, null=False, max_length=128, default='')
    ceilings = models.CharField(verbose_name='Потолки', blank=True, null=False, max_length=128, default='')
    parking = models.CharField(verbose_name='Паркинг', blank=True, null=False, max_length=128, default='')
    parking_price = models.CharField(verbose_name='Паркинг, р', blank=True, null=False, max_length=64, default='')
    trade_registration = models.CharField(verbose_name='Регистрация сделки', blank=True, null=False, max_length=128, default='')
    mortgage = models.CharField(verbose_name='Ипотека', blank=True, null=False, max_length=128, default='')
    installment = models.CharField(verbose_name='Рассрочка', blank=True, null=False, max_length=128, default='')
    promotions = models.CharField(verbose_name='Акции', blank=True, null=False, max_length=256, default='')
    complex_infrastructure = models.CharField(verbose_name='Инфраструктура комплекса', blank=True, null=False, max_length=256, default='')
    commercial_space = models.CharField(verbose_name='Коммерческие площади', blank=True, null=False, max_length=128, default='')
    # Закрытые для клиента данные
    weekdays_from = models.IntegerField(null=False, blank=True, verbose_name='Будни с', default=9)
    weekdays_to = models.IntegerField(null=False, blank=True, verbose_name='Будни по', default=18)
    weekend_form = models.IntegerField(null=False, blank=True, verbose_name='Выходные с', default=9)
    weekend_to = models.IntegerField(null=False, blank=True, verbose_name='Выходные по', default=18)
    sales_office_address = models.TextField(null=False, default='', blank=True, verbose_name='Адрес офиса продаж', max_length=256)
    note = models.TextField(null=False, default='', blank=True, verbose_name='Примечание', max_length=516)
    parking_close = models.TextField(null=False, default='', blank=True, verbose_name='Паркинг', max_length=256)



    class Meta:
        verbose_name = 'ЖК'
        verbose_name_plural = 'ЖК'
        ordering = ['name']

    def __str__(self):
        return self.name



class Corp(models.Model):
    updated_by = models.ForeignKey(User, verbose_name='Кем изменена', on_delete=models.DO_NOTHING, \
                                   blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')
    name = models.CharField(verbose_name='Название', blank=True, null=False, max_length=128, default='')
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', related_name='floors',
                                 on_delete=models.CASCADE, blank=False, null=False)
    start_of_construction = models.DateField(blank=False, null=True, verbose_name='Начало строительства')
    end_of_construction = models.DateField(blank=False, null=True, verbose_name='Сдача')
    premises_type = models.ForeignKey('crm.PremisesType', verbose_name='Тип помещения', null=True, \
                                      on_delete=models.SET_NULL)
    count_lots = models.IntegerField(verbose_name='Количество лотов', blank=False, null=True)
    count_floors = models.IntegerField(verbose_name='Этажность', blank=True, null=True)

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпусы'

    def __str__(self):
        return self.name or self.complex



class Floor(models.Model):
    updated_by = models.ForeignKey(User, verbose_name='Кем изменена', on_delete=models.DO_NOTHING, \
                                   blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')

    name = models.CharField(verbose_name='Название', blank=True, null=False, max_length=128, default='')
    plan = models.ImageField(upload_to=images_upload_path, blank=True, null=True, verbose_name='Планировка')

    class Meta:
        verbose_name = 'План этажа'
        verbose_name_plural = 'Планы этажей'

    def __str__(self):
        return self.name or 'Планировка этажа №{0}'.format(self.id)

    def image_tag(self):
        if self.plan:
            return mark_safe('<img src="/media/%s" width="350" height="auto" />' % (self.plan))
        return 'Изображение отсутствует'

    image_tag.short_description = 'Image'


class Layout(models.Model):
    corp = models.ForeignKey('crm.Corp', verbose_name='Корпус', null=True, blank=True, on_delete=models.CASCADE)
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', null=True, blank=True, on_delete=models.CASCADE)
    floor_from = models.IntegerField(verbose_name='Этаж с', null=False, blank=False, default=0)
    floor_to = models.IntegerField(verbose_name='Этаж по', null=False, blank=False, default=0)
    floor = models.ForeignKey('crm.Floor', verbose_name='Планировка эатажа', null=False, blank=False, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'План этажа'
        verbose_name_plural = 'Планы этажей'

    def __str__(self):
        return 'Планировка в {0}'.format(self.corp)

