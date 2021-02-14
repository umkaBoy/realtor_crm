from crm import models
from django.contrib.admin import TabularInline


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
