from rest_framework import serializers
from blogs.models import Tag, Post, Comment
from utils.serializers import RecursiveField


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'comments_count']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveField(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'caption',
            'created',
            'updated',
            'children'
        ]
        read_only_fields = [
            'id', 
            'post', 
            'created',
            'updated',
            'children'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
