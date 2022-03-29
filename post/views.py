from rest_framework import permissions, generics

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
