from django.urls import path, include

from rest_framework import routers
from .views import UsersViewset, ProfileViewset

router = routers.SimpleRouter()
router.register('users', UsersViewset, basename='users-api')
router.register('profiles', ProfileViewset, basename='profiles-api')


urlpatterns = [
    path('auth/', include(router.urls)),
]