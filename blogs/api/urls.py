from django.urls import path, include

from rest_framework import routers
from .views import PostViewset, CommentViewset, TagViewset

router = routers.SimpleRouter()
router.register('posts', PostViewset, basename='posts-api')
router.register('comments', CommentViewset, basename='comments-api')
router.register('tags', TagViewset, basename='tag-api')


urlpatterns = [
    path('blogs/', include(router.urls)),
]

