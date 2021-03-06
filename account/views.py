from django.contrib.auth import get_user_model

from rest_framework import permissions, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from . import serializers


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserLoginSerializer

    def post(self, request, *args, **kwargs):
        ser = serializers.UserLoginSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        try:
            user = get_user_model().objects.get(
                username=ser.validated_data.get('username'),
            )

            if not user.check_password(ser.validated_data.get('password')):
                raise

        except Exception as e:
            return Response({
                'msg': 'No active account found with the given credentials',
            }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': str(token),
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_pic': user.profile_pic.url,
                'phone_number': user.phone_number,
            }, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'msg': "Done"
        }, status=status.HTTP_201_CREATED, headers=headers)
