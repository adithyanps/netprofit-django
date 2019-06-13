from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, authentication, permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status
from rest_framework import views
from rest_framework import filters
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

# journal entry

class AccountViewset(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("type",)

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


class SalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.SalesInvoice.objects.all()
    serializer_class = serializers.ParantInvoiceSerializerTest

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


class CustomerReceiptViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerReceiptSerializer
    queryset = models.CustomerReceipt.objects.all()

    def get_queryset(self):
        """return objects"""
        return self.queryset.order_by('id')


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExpenseCategorySerializer
    queryset = models.ExpenseCategory.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('id')


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExpenseSerializer
    queryset = models.Expenses.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('id')
