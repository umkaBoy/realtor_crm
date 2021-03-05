from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from crm.models import Developer, Complex, NewBuildingLot, OldBuildingLot, Image, Contacts


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'id',
            'get_url'
        )


class ContactsSerializer(ModelSerializer):

    class Meta:
        model = Contacts
        fields = (
            'id',
            'name',
            'phone',
            'email',
            'note',
        )


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff'
        )


class DeveloperSubSerializer(ModelSerializer):

    class Meta:
        model = Developer
        fields = (
            'id',
            'name',
            'count_complexes'
        )


class ComplexSubSerializer(ModelSerializer):

    class Meta:
        model = Complex
        fields = (
            'id',
            'name',
            'count_lots_in_sale'
        )


class ComplexesShortSerializer(ModelSerializer):
    developer = DeveloperSubSerializer()

    class Meta:
        model = Complex
        fields = (
            'id',
            'name',
            'developer',
            'end_of_construction',
            'address'
        )


class OldBuildingsShortSerializer(ModelSerializer):
    complex = ComplexSubSerializer()

    class Meta:
        model = OldBuildingLot
        fields = (
            'id',
            '__str__',
            'status',
            'floor',
            's',
            'type_building',
            'price',
            'complex',
            'url_plan'
        )


class NewBuildingsShortSerializer(ModelSerializer):
    complex = ComplexSubSerializer()

    class Meta:
        model = NewBuildingLot
        fields = (
            'id',
            'type_building',
            '__str__',
            'status',
            'floor',
            's',
            'price',
            'complex',
            'url_plan'
        )


class MainDeveloperSerializer(ModelSerializer):
    updated_by = ProfileSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()
    contacts = ContactsSerializer(many=True, read_only=True)

    def get_description(self, instance):
        from django.utils.safestring import mark_safe
        return mark_safe(instance.description)

    class Meta:
        model = Developer
        fields = (
            'id',
            'contacts',
            'updated_by',
            'updated_at',
            'name',
            'created_at',
            'description',
            'objects_delivered',
            'objects_under_construction',
            'images'
        )


class MainComplexSerilizer(ModelSerializer):
    updated_by = ProfileSerializer(read_only=True)

    class Meta:
        model = Complex
        fields = (
            'id',
            'updated_by',
            'updated_at'
        )


class MainOldSerilizer(ModelSerializer):
    updated_by = ProfileSerializer(read_only=True)

    class Meta:
        model = OldBuildingLot
        fields = (
            'id',
            'updated_by',
            'updated_at'
        )


class MainNewSerilizer(ModelSerializer):
    updated_by = ProfileSerializer(read_only=True)

    class Meta:
        model = NewBuildingLot
        fields = (
            'id',
            'updated_by',
            'updated_at'
        )