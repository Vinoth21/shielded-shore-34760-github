from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from orderapp.serializers import  MenuSerializer, OrderSerializer, UserObjectSerializer #, UserSerializer
from .models import Menu, UserObjects
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


class MenuViewset(viewsets.ModelViewSet):

    queryset = Menu.objects.all().order_by('-votes')
    serializer_class = MenuSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
         try:
            if self.request.user.is_superuser:
                serializer.save()
         except:
             raise PermissionDenied
             #print ("Only admin has the privilage")
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
        else:
            permission_classes = (permissions.IsAdminUser,)
        return [permission() for permission in permission_classes]


class MenuDetailViewset(viewsets.ModelViewSet):

    queryset = Menu.objects.all().order_by('-votes')
    serializer_class = MenuSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
        else:
            permission_classes = (permissions.IsAdminUser,)
        return [permission() for permission in permission_classes]



class UserObjectViewset(viewsets.ModelViewSet):
    queryset = UserObjects.objects.all()
    serilizer_class = UserObjectSerializer
    permission_class = (permissions.IsAuthenticated)

    def perform_create(self):
        pass

class OrderViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('-votes')[:1]
    serializer_class = OrderSerializer
    #permission_class = (permissions.IsAdminUser)
  
    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
        else:
            permission_classes = (permissions.IsAdminUser,)
        return [permission() for permission in permission_classes]


"""

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""