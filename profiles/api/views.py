from rest_framework import viewsets
from django.contrib.auth import get_user_model
from profiles.models import Profile
from .serializers import ProfileSerializer, UserSerializer

User = get_user_model()


class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class UsersViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
