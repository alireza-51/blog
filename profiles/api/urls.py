from django.urls import path, include

from rest_framework import routers
from .views import (
    UsersRetrieveUpdateDestroyView, 
    UsersCreateView, 
    ProfileRetrieveUpdateDestroyView, 
    ProfileCreateView, 
    CurrentProfileView,
    CurrentUsersView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# router = routers.SimpleRouter()
# router.register('users', UsersViewset, basename='users-api')
# router.register('profiles', ProfileViewset, basename='profiles-api')


urlpatterns = [
    path('users/<int:pk>/', UsersRetrieveUpdateDestroyView.as_view(),
         name='retrieve-update-destroy-user'),
    path('users/', UsersCreateView.as_view(), name='create-user'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(),
         name='retrieve-update-destroy-profile'),
    path('profiles/', ProfileCreateView.as_view(), name='create-profile'),

    path('current-user/', CurrentUsersView.as_view(), name='current-user'),
    path('current-profile/', CurrentProfileView.as_view(), name='current-profile'),
    # JWT routes
    path('auth/login/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/login/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
