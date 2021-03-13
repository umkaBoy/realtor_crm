from django.db import models
from crm.utils.base import documents_upload_path, images_upload_path
from crm.consts import *
import os
import datetime


class Region(models.Model):
    name = models.CharField(verbose_name='Название региона', blank=False, null=False, max_length=128)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ['name']

    def __str__(self):
        return self.name



class ConstructionTech(models.Model):
    name = models.CharField(verbose_name='Технология строительства', blank=False, null=False, max_length=128)

    class Meta:
        verbose_name = 'Технология строительства'
        verbose_name_plural = 'Технологии строительства'
        ordering = ['name']

    def __str__(self):
        return self.name


class PremisesType(models.Model):
    name = models.CharField(verbose_name='Тип помещения', blank=False, null=False, max_length=128)

    class Meta:
        verbose_name = 'Тип помещения'
        verbose_name_plural = 'Типы помещения'
        ordering = ['name']

    def __str__(self):
        return self.name


class ObjectClass(models.Model):
    name = models.CharField(verbose_name='Класс объекта', blank=False, null=False, max_length=128)

    class Meta:
        verbose_name = 'Класс объекта'
        verbose_name_plural = 'Классы объектов'
        ordering = ['name']

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(verbose_name='Контактное лицо', blank=True, null=False, max_length=128, default='')
    phone = models.CharField(verbose_name='Телефон', blank=True, null=False, max_length=128, default='')
    email = models.EmailField(verbose_name='E-mail', blank=True, null=False, max_length=64, default='')
    note = models.CharField(verbose_name='Примечание', blank=True, null=False, max_length=256, default='')
    developer = models.ForeignKey('crm.Developer', verbose_name='Застройщик', related_name='contacts', on_delete=models.CASCADE, \
                                 blank=True, null=True)
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', related_name='contacts',
                                  on_delete=models.CASCADE, blank=True, null=True)
    lot = models.ForeignKey('crm.Lot', verbose_name='Лот', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['name']

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(verbose_name='Название', blank=True, null=False, max_length=30, default='')
    link = models.CharField(verbose_name='Ссылка', max_length=128, null=False, blank=True, default='')
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', related_name='links', null=True, on_delete=models.CASCADE)
    lot = models.ForeignKey('crm.Lot', verbose_name='Лот', null=True, on_delete=models.CASCADE)
    developer = models.ForeignKey('crm.Developer', verbose_name='застройщик', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['name']


    def __str__(self):
        return self.name



class Document(models.Model):
    file = models.FileField(upload_to=documents_upload_path, max_length=512, verbose_name='Файл')
    type = models.CharField(max_length=64, choices=DOCUMENT_TYPES, verbose_name='Тип документа')
    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', related_name='files', null=True, on_delete=models.CASCADE)
    lot = models.ForeignKey('crm.Lot', verbose_name='Лот', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['type']


    def __str__(self):
        return self.filename


    @property
    def get_size(self):
        if os.path.exists(self.file.path):
            return "%0.1f KB" % (os.path.getsize(self.file.path) / (1024.0))
        return "0 MB"

    get_size.fget.short_description = u'Размер'

    @property
    def get_created_at(self):
        if self.file:
            statbuf = os.stat(self.file.path)
            return datetime.datetime.utcfromtimestamp(statbuf.st_ctime).date()
        return ''

    get_created_at.fget.short_description = u'Дата загрузки'


    @property
    def get_url(self):
        if self.file:
            return self.file.url
        return ''

    @property
    def filename(self):
        return os.path.basename(self.file.name)



class Image(models.Model):
    image = models.ImageField(upload_to=images_upload_path, null=False, verbose_name='Изображение')

    complex = models.ForeignKey('crm.Complex', verbose_name='ЖК', related_name='images', null=True, on_delete=models.CASCADE)
    lot = models.ForeignKey('crm.Lot', verbose_name='Лот', null=True, on_delete=models.CASCADE)
    developer = models.ForeignKey('crm.Developer', related_name='images', verbose_name='Застройщик', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return 'image_' + str(self.id)


    @property
    def get_size(self):
        if os.path.exists(self.image.path):
            return "%0.1f KB" % (os.path.getsize(self.image.path) / (1024.0))
        return "0 MB"

    get_size.fget.short_description = u'Размер'



    @property
    def get_created_at(self):
        if os.path.exists(self.image.path):
            statbuf = os.stat(self.image.path)
            return datetime.datetime.utcfromtimestamp(statbuf.st_ctime).date()
        return ''

    get_created_at.fget.short_description = u'Дата загрузки'


    @property
    def get_url(self):
        if self.image:
            return self.image.url
        else:
            return ''

