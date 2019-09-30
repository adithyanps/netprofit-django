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
from Customer_Receipts import models
from Customer_Receipts import serializers
# from . import Permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters import FilterSet
import django_filters
from django_filters import rest_framework as filters
import calendar

from Utility import Utility

# Create your views here.

# class CustomerReceiptFilter(FilterSet):
#     start_date = filters.DateFilter(method="filter_by_start_date")
#     end_date = filters.DateFilter(method="filter_by_end_date")
#     class Meta:
#         model = models.CustomerReceipt
#         fields = "__all__"
#         lookup_fields = ["journal_entry","journal_item","partner"]
#         # fields = ["customer","date"]
#
#     def filter_by_start_date(self, queryset, name, value):
#         queryset = queryset.filter(journal_entry__date__gte = value)
#         return queryset
#
#     def filter_by_end_date(self, queryset, name, value):
#         queryset = queryset.filter(journal_entry__date__lte = value)
#         return queryset
#


class CustomerReceiptViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerReceiptSerializer
    queryset = models.CustomerReceipt.objects.all()
    # filter_backends = (DjangoFilterBackend,OrderingFilter, SearchFilter)
    # filter_class = CustomerReceiptFilter
    # search_fields = ('date',)

    def get_queryset(self):
        """return objects"""
        return self.queryset.order_by('id')

    def create(self,request, *args, **kwargs):
        print(request.data,"ddata")
        doc = request.data['reciept_no']
        print(doc)
        if doc==None:
            request.data['reciept_no']=Utility.autoRecieptNumberGenerator()

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
