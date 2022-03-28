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
            token = Token.objects.filter(user=user)
            if token.exists():
                token = token.first()
            else:
                token = Token.objects.create(user=user)
            return Response({
                'token': str(token)
            }, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserRegisterSerializer
