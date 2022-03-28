from rest_framework import permissions, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from . import serializers
from . import models


class NewPostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PostSerializer


class PostByCityView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        city = self.kwargs.get('city')
        return models.Post.objects.filter(city__title__iexact=city)
