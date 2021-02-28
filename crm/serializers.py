from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from crm.models import Developer, Complex, NewBuildingLot, OldBuildingLot


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
            'count_floors'
        )


class OldBuildingsShortSerializer(ModelSerializer):
    complex = ComplexSubSerializer()

    class Meta:
        model = OldBuildingLot
        fields = (
            'id',
            'name',
            'status',
            'floor',
            's',
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
            'name',
            'status',
            'floor',
            's',
            'price',
            'complex',
            'url_plan'
        )