from rest_framework import viewsets, permissions
from blogs.models import Post, Tag, Comment

from .serializers import PostSerializer, CommentSerializer, TagSerializer
from utils.custom_permissions import IsAuthorOrCreateOrReadOnly

class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthorOrCreateOrReadOnly]


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrCreateOrReadOnly]


class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
