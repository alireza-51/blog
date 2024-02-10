from django.urls import path, include

from rest_framework import routers
from .views import UsersViewset, ProfileViewset

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.SimpleRouter()
router.register('users', UsersViewset, basename='users-api')
router.register('profiles', ProfileViewset, basename='profiles-api')


urlpatterns = [
    path('auth/', include(router.urls)),
    # JWT routes
    path('auth/login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]