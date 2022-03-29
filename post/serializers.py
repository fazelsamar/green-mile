from rest_framework import serializers

from . import models

from location.models import City
from account.models import MyUser


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostImage
        fields = [
            # 'title',
            'image',
        ]


class PostCommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=MyUser.objects.all(),
    )

    class Meta:
        model = models.PostComment
        fields = [
            'body',
            'user',
        ]


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(
        source='postimage_set',
        many=True,
        read_only=True
    )
    city = serializers.SlugRelatedField(
        slug_field='title',
        queryset=City.objects.all(),
    )
    comments = PostCommentSerializer(
        source='postcomment_set',
        many=True,
        read_only=True
    )
    likes = serializers.SerializerMethodField('get_likes')

    class Meta:
        model = models.Post
        fields = [
            'id',
            'title',
            'image',
            'description',
            'postal_address',
            'city',
            'location',
            'images',
            'comments',
            'likes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

    def get_likes(self, obj):
        return obj.postlike_set.all().count()

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        # print(self.context.get('view').request.FILES['images'])
        post = models.Post.objects.create(**validated_data)
        for image_data in images_data.values():
            models.PostImage.objects.create(post=post, image=image_data)
        return post


class NewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostComment
        fields = [
            'body',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        post = self.context['post']
        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(
            **validated_data,
            user=user,
            post=post,
        )
        return instance
