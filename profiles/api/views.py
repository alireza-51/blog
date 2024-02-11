from rest_framework import views, permissions, generics, response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from profiles.models import Profile
from .serializers import ProfileSerializer, UserSerializer

User = get_user_model()


class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(user=self.request.user)
        

class CurrentProfileView(views.APIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        try:
            profile = Profile.objects.get(user=self.request.user)
            data = self.serializer_class(profile).data
            return response.Response(data)
        except Profile.DoesNotExist:
            return response.Response(data={'DoesNotExist': 'Profile Does Not Exist'}, status=404)
      
        
class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = []
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class UsersRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)


class CurrentUsersView(views.APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        data = self.serializer_class(request.user).data
        return response.Response(data)


class UsersCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []
    queryset = User.objects.all()
