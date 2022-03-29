from rest_framework import permissions, generics

from . import serializers
from . import models


class ProvincesView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProvinceSerializer
    queryset = models.Province.objects.all()
