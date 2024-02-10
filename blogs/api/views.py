from rest_framework import viewsets
from blogs.models import Post, Tag, Comment

from .serializers import PostSerializer, CommentSerializer, TagSerializer


class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
