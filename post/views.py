from django.shortcuts import get_object_or_404

from rest_framework import permissions, status, generics
from rest_framework.response import Response
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


class NewCommentView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.NewCommentSerializer

    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(models.Post, id=post_id)
        new_comment_ser = serializers.NewCommentSerializer(data=request.data, context={
            'request': request,
            'post': post,
        })
        new_comment_ser.is_valid(raise_exception=True)
        new_ticket_obj = new_comment_ser.create(
            validated_data=new_comment_ser.validated_data
        )
        return Response(new_comment_ser.data, status=status.HTTP_201_CREATED)


class NewCommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(models.Post, id=post_id)
        user = request.user
        like, created = models.PostLike.objects.get_or_create(
            user=user, post=post)
        if created:
            return Response({
                'msg': 'user already likes this post'
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'msg': 'Done'
        }, status=status.HTTP_200_OK)
