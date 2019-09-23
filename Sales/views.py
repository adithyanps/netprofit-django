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
from Sales import models
from Sales import serializers
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

class SalesInvoiceFilter(FilterSet):
    # customer = CharFilter('customer')
    start_date = filters.DateFilter(method="filter_by_start_date")
    end_date = filters.DateFilter(method="filter_by_end_date")

    class Meta:
        model = models.SalesInvoice
        fields = "__all__"
        # fields = ["customer","date"]

    def filter_by_start_date(self, queryset, name, value):
        queryset = queryset.filter(date__gte = value)
        return queryset

    def filter_by_end_date(self, queryset, name, value):
        queryset = queryset.filter(date__lte = value)
        return queryset


class SalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.SalesInvoice.objects.all()
    serializer_class = serializers.SalesInvoiceSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter, SearchFilter)
    filter_class = SalesInvoiceFilter
    search_fields = ('date',"customer")


    def get_queryset(self):
        return self.queryset.order_by('id')


class InvoiceLineViewSet(viewsets.ModelViewSet):
    queryset = models.InvoiceLine.objects.all()
    serializer_class = serializers.InvoiceLineSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')
