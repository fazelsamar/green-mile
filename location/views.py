from rest_framework import permissions, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from . import serializers
from . import models


class ProvincesView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProvinceSerializer
    queryset = models.Province.objects.all()
