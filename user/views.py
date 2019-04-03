from django.shortcuts import render
from rest_framework import generics
from user.serializers import UserSerializer
from rest_framework import generics
from django.views import View
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.contrib.auth import get_user_model
from rest_framework import filters

from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework import generics, authentication, permissions
# Create your views here.

class CreateUserView(generics.ListCreateAPIView):
    """Create a new user in the system"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","email")


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
