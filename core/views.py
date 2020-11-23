from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from core import models, serializers
from rest_framework.authentication import TokenAuthentication
from core import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class TasksViewSet(viewsets.ModelViewSet):
     authentication_classes = (TokenAuthentication,)
     serializer_class = serializers.TasksSerializer
     queryset = models.Tasks.objects.all()
     permission_classes = (
         permissions.UpdateOwnStatus,
         IsAuthenticatedOrReadOnly
     )
     
     def perform_create(self,serializer):
         serializer.save(user_profile=self.request.user)

class addCarViewSet(viewsets.ModelViewSet):
     authentication_classes = (TokenAuthentication,)
     serializer_class = serializers.AddCarSerializer
     queryset = models.Car.objects.all()
     permission_classes = (
         permissions.UpdateOwnStatus,
         IsAuthenticatedOrReadOnly
     )
     
     def perform_create(self,serializer):
         serializer.save(user_profile=self.request.user)