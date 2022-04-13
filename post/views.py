from django.shortcuts import get_object_or_404

from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from . import serializers
from . import models


class NewPostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PostSerializer


class PostByProvinceView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        province = self.kwargs.get('province')
        return models.Post.objects.filter(province__title__iexact=province)


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


class ToggleLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(models.Post, id=post_id)
        user = request.user
        like_obj, created = models.PostLike.objects.get_or_create(
            user=user, post=post)
        if not created:
            like_obj.delete()
            return Response({
                'msg': 'Unliked'
            }, status=status.HTTP_200_OK)

        return Response({
            'msg': 'Liked'
        }, status=status.HTTP_200_OK)


class NewWelfarePlaceView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PostWelfarePlaceSerializer

    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(models.Post, id=post_id)
        if not request.user == post.user:
            return Response({
                "msg": "User is not owner of this post",
            }, status=status.HTTP_400_BAD_REQUEST)
        new_welfare_place_ser = serializers.PostWelfarePlaceSerializer(data=request.data, context={
            'request': request,
            'post': post,
        })
        new_welfare_place_ser.is_valid(raise_exception=True)
        new_welfare_place_obj = new_welfare_place_ser.create(
            validated_data=new_welfare_place_ser.validated_data
        )
        return Response(new_welfare_place_ser.data, status=status.HTTP_201_CREATED)


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    # .prefetch_related('postimage') \
    # .prefetch_related('postcomment') \
    # .prefetch_related('postlike') \
    # .prefetch_related('postwelfareplace')

    serializer_class = serializers.PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['province__title']
    search_fields = ['title']
    ordering_fields = ['updated_at', 'id']
    permission_classes = [permissions.AllowAny]


class PostRetrieve(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]
