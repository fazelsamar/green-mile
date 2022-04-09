from rest_framework import serializers

from . import models


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MyUser
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'profile_pic',
            'phone_number',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = models.MyUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
