from django.shortcuts import render

from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, authentication, permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status
from rest_framework import views
# from rest_framework import filters
from itertools import zip_longest as zip
from collections import defaultdict
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import json
from Masters import models
from Masters import serializers
# from . import Permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters import FilterSet
import django_filters
from django_filters import rest_framework as filters
import calendar

# Create your views here.
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer

    filter_backends = (SearchFilter,)
    search_fields = ("name",)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')


class BranchViewset(viewsets.ModelViewSet):
    """create ,delete ,edit and view branch"""
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer

    """filter option on api"""
    filter_backends = (SearchFilter,)
    search_fields = ("branch",)

    def get_queryset(self):
        """return objects"""
        return self.queryset.order_by('id')
class AreaViewSet(viewsets.ModelViewSet):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer

    filter_backends = (SearchFilter,)
    search_fields = ("area",)

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer

    filter_backends = (SearchFilter,)
    search_fields = ("name",)

    def get_queryset(self):
        """return objects"""
        return self.queryset.order_by('id')


class ProductViewset(viewsets.ModelViewSet):
    """create a new item and see all items"""
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    filter_backends = (SearchFilter,)
    search_fields = ("item",)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')

# journal entry

class AccountViewset(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

    filter_backends = (SearchFilter,)
    search_fields = ("type",)
    filter_fields = ("type",)


    def get_queryset(self):
        return self.queryset.order_by('id')

class AccountDefaultViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AccountDefaultSerializer
    queryset = models.AccountDefault.objects.all()
    # authentication_classes = (authentication.TokenAuthentication,)
    # def get_queryset(self):
    #     if (self.request.user.user_choice == "FULL_ACCESS"):
    #         return self.queryset
    #     return None
