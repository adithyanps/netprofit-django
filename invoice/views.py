from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from itertools import zip_longest as zip
import calendar
from collections import defaultdict
from django.http import JsonResponse

from core import models
from invoice import serializers

# Create your views here.
class CustomerViewset(viewsets.ModelViewSet):
    """create ,delete ,edit and view customers"""
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

    """search json data on api"""
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')


class BranchViewset(viewsets.ModelViewSet):
    """create ,delete ,edit and view branch"""
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer

    """filter option on api"""
    filter_backends = (filters.SearchFilter,)
    search_fields = ("branch",)

    def get_queryset(self):
        """return objects"""
        return self.queryset.order_by('id')


class ItemViewset(viewsets.ModelViewSet):
    """create a new item and see all items"""
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemsSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("item",)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')


class C_InvoiceViewset(viewsets.ModelViewSet):
    """created a view for nested serializer-child data"""

    queryset = models.C_Invoice.objects.all()
    serializer_class = serializers.C_InvoiceSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("item","key")


class P_InvoiceViewset(viewsets.ModelViewSet):
    """created a view for nested serializer - parent data"""

    queryset = models.P_Invoice.objects.all()
    serializer_class = serializers.P_InvoiceSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')
