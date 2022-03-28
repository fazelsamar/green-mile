from rest_framework import serializers

from . import models

from location.models import City


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostImage
        fields = [
            # 'title',
            'image',
        ]


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(
        source='postimage_set', many=True, read_only=True)
    city = serializers.SlugRelatedField(
        slug_field='title',
        queryset=City.objects.all(),
    )

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
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        post = models.Post.objects.create(**validated_data)
        for image_data in images_data.values():
            models.PostImage.objects.create(post=post, image=image_data)
        return post


class PostCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostComment
        fields = [
            'title',
            'user',

        ]
