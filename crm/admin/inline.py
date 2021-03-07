from crm import models
from django.contrib.admin import TabularInline
from django.utils.safestring import mark_safe


class ContactsInlineAdmin(TabularInline):
    extra = 0
    model = models.Contacts
    fields = ['name', 'email', 'phone', 'note']


class LinkInlineAdmin(TabularInline):
    extra = 0
    model = models.Link
    fields = ['name', 'link']


class LayoutInlineAdmin(TabularInline):
    extra = 0
    model = models.Layout
    fields = ['floor', 'floor_from', 'floor_to']


class DocumentInlineAdmin(TabularInline):
    extra = 0
    model = models.Document
    readonly_fields = ['get_created_at', 'get_size']
    fields = ['type', 'name', 'file', 'get_created_at', 'get_size']


class ImageInlineAdmin(TabularInline):
    extra = 0
    model = models.Image
    readonly_fields = ('image_preview',)
    readonly_fields = ['get_created_at', 'get_size', 'image_preview']
    fields = ['image', 'get_created_at', 'get_size', 'image_preview']


    def image_preview(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe(
                '<img src="{0}" width="250" height="auto" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return '(No image)'

    image_preview.short_description = 'Preview'
