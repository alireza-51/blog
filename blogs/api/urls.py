from django.urls import path, include

from rest_framework import routers
from .views import PostViewset, CommentListCreate, CommentRetrieveUpdateDestroyView, TagViewset

router = routers.SimpleRouter()
router.register('posts', PostViewset, basename='posts-api')
router.register('tags', TagViewset, basename='tag-api')


urlpatterns = [
    path('blogs/', include(router.urls)),
    path('blogs/comments/<int:post_id>/', CommentListCreate.as_view(), name='list-create-comment'),
    path('blogs/comment/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-comment')
]
