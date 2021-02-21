from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


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