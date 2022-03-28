from rest_framework import serializers

from . import models


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MyUser
        fields = ['username', 'password']