from django.shortcuts import render

# Create your views here.
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
from Expenses import models
from Expenses import serializers
# from . import Permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters import FilterSet
import django_filters
from django_filters import rest_framework as filters
import calendar


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExpenseCategorySerializer
    queryset = models.ExpenseCategory.objects.all()

    filter_backends = (SearchFilter,)
    search_fields = ("name",)

    def get_queryset(self):
        return self.queryset.order_by('id')


class ExpenseFilter(FilterSet):
    # customer = CharFilter('customer')
    start_date = filters.DateFilter(method="filter_by_start_date")
    end_date = filters.DateFilter(method="filter_by_end_date")

    class Meta:
        model = models.Expenses
        fields = "__all__"
        # fields = ["customer","date"]

    def filter_by_start_date(self, queryset, name, value):
        queryset = queryset.filter(Date__gte = value)
        return queryset

    def filter_by_end_date(self, queryset, name, value):
        queryset = queryset.filter(Date__lte = value)
        return queryset


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExpenseSerializer
    queryset = models.Expenses.objects.all()

    filter_backends = (DjangoFilterBackend,OrderingFilter, SearchFilter)
    filter_class = ExpenseFilter
    search_fields = ('Date',"ExpenseCategory","ExpenseAcct")

    def get_queryset(self):
        return self.queryset.order_by('id')
