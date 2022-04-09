from rest_framework import serializers

from . import models

from location.models import Province
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

    profile_pic = serializers.SerializerMethodField('get_profile_pic')

    class Meta:
        model = models.PostComment
        fields = [
            'body',
            'user',
            'profile_pic',
        ]

    def get_profile_pic(self, obj):
        return obj.user.profile_pic.url


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(
        source='postimage_set',
        many=True,
        read_only=True
    )
    province = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Province.objects.all(),
    )
    comments = PostCommentSerializer(
        source='postcomment_set',
        many=True,
        read_only=True
    )
    likes = serializers.SerializerMethodField('get_likes')
    does_user_likes = serializers.SerializerMethodField('get_does_user_likes')

    class Meta:
        model = models.Post
        fields = [
            'id',
            'title',
            'image',
            'description',
            'postal_address',
            'province',
            'location',
            'images',
            'location_kind',
            'rest_place',
            'comments',
            'likes',
            'does_user_likes',
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

    def get_does_user_likes(self, obj):
        user = self.context.get('request').user
        if user.pk:
            return obj.postlike_set.filter(user=user).exists()
        return "User not loged in"

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
