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
from core import models
from invoice import serializers
from . import Permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters import FilterSet
import django_filters
from django_filters import rest_framework as filters

# Create your views here.
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer

    filter_backends = (SearchFilter,)
    search_fields = ("name",)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')
        
class CustomerViewset(viewsets.ModelViewSet):
    """create ,delete ,edit and view customers"""
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

    """search json data on api"""
    filter_backends = (SearchFilter,)
    search_fields = ("customer",)

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


class ItemViewset(viewsets.ModelViewSet):
    """create a new item and see all items"""
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemsSerializer

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


class JournalItemViewset(viewsets.ModelViewSet):
    queryset = models.JournalItem.objects.all()
    serializer_class = serializers.JournalItemSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')


class JournalEntryViewset(viewsets.ModelViewSet):
    queryset = models.JournalEntry.objects.all()
    serializer_class = serializers.JournalEntrySerializer

    def get_queryset(self):
        return self.queryset.order_by('id')

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
    serializer_class = serializers.ParantInvoiceSerializerTest
    filter_backends = (DjangoFilterBackend,OrderingFilter, SearchFilter)
    filter_class = SalesInvoiceFilter
    search_fields = ('date',"customer")


    def get_queryset(self):
        return self.queryset.order_by('id')


class ParentInvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Parent.objects.all()
    serializer_class = serializers.ParentInvoiceSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')



class InvoiceLineViewSet(viewsets.ModelViewSet):
    queryset = models.InvoiceLine.objects.all()
    serializer_class = serializers.InvoiceLineSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')


class ChildInvoiceViewset(viewsets.ModelViewSet):
    """created a view for nested serializer - parent data"""

    queryset = models.ChildInvoice.objects.all()
    serializer_class = serializers.ChildInvoiceSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('id')


class AccountDefaultViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AccountDefaultSerializer
    queryset = models.AccountDefault.objects.all()
    # authentication_classes = (authentication.TokenAuthentication,)
    # def get_queryset(self):
    #     if (self.request.user.user_choice == "FULL_ACCESS"):
    #         return self.queryset
    #     return None

class CustomerReceiptFilter(FilterSet):
    start_date = filters.DateFilter(method="filter_by_start_date")
    end_date = filters.DateFilter(method="filter_by_end_date")
    class Meta:
        model = models.CustomerReceipt
        fields = "__all__"
        lookup_fields = ["journal_entry","journal_item","partner"]
        # fields = ["customer","date"]

    def filter_by_start_date(self, queryset, name, value):
        queryset = queryset.filter(journal_entry__date__gte = value)
        return queryset

    def filter_by_end_date(self, queryset, name, value):
        queryset = queryset.filter(journal_entry__date__lte = value)
        return queryset



class CustomerReceiptViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerReceiptSerializer
    queryset = models.CustomerReceipt.objects.all()
    filter_backends = (DjangoFilterBackend,OrderingFilter, SearchFilter)
    filter_class = CustomerReceiptFilter
    search_fields = ('date',)

    def get_queryset(self):
        """return objects"""
        return self.queryset.order_by('id')


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
