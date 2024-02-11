from django.db.models import Count
from rest_framework import viewsets, generics, permissions, response, status
from blogs.models import Post, Tag, Comment

from .serializers import PostSerializer, CommentSerializer, TagSerializer
from utils.custom_permissions import PostAuthorOrCreateOrReadOnly, CommentAuthor

class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(comments_count=Count('comments'))
    permission_classes = [PostAuthorOrCreateOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(parent__isnull=True)
    permission_classes = []

    def list(self, request, post_id, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(post=post_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    
    def perform_create(self, serializer, post_id):
        serializer.save(author=self.request.user, post=Post.objects.get(id=post_id))
    
    def create(self, request, post_id, *args, **kwargs):
        # data = request.data
        # data._mutable = True
        # data.update({'post_id':post_id})
        # data._mutable = False

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, post_id)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [CommentAuthor]

    def list(self, request, post_id, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(post=post_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
