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

# journal entry

class AccountViewset(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

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


# class Sample(View):
#     @csrf_exempt
#     def dispatch(self, *args, **kwargs):
#         # import ipdb; ipdb.set_trace()
#         return super().dispatch(*args, **kwargs)
#
#     def foo_bar(self,http_res):
#         print(http_res,'/////')
#         return http_res
#
#     def post(self, request):
#         result = request.body
#         http_response = HttpResponse(result)
#         self.foo_bar(result)
#         return http_response



class ParentInvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Parent.objects.all()
    serializer_class = serializers.ParentInvoiceSerializer


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


class ReceiptView(APIView):
    def get(self, request):
        receipt_id=request.GET.get('id')
        response_data = {}
        journal_entry = {}
        child={}
        try:
            receipt=CustomerReceipt.objects.get(reciept_no=receipt_id)
            response_data["id"]=receipt.id
            jentry=receipt.journal_entry
            journal_entry["date"]=str(jentry.date)
            journal_entry["transaction_type"]=jentry.transaction_type
            journal_entry["description"]=jentry.description
            childs=JournalItem.objects.filter(journal_entry=jentry)
            child=[dict(account=str(c.account.name),partner=str(c.partner),debit_amount=str(c.debit_amount),credit_amount=str(c.credit_amount)) for c in childs]
            journal_entry["child"]=child
            response_data["journal_entry"]=journal_entry
            response_data["receipt_number"]=receipt.reciept_no
        except:
            pass
        return Response(response_data)

class JournalITEMViewset(viewsets.ModelViewSet):
    queryset = models.JournalItems.objects.all()
    serializer_class = serializers.JournalItemsSerializer

class JournalEntriesviewset(viewsets.ModelViewSet):
    queryset = models.JournalEntries.objects.all()
    serializer_class = serializers.JournalEntriesSerializer

class CustomerReceiptsViewSet(viewsets.ModelViewSet):
    queryset = models.CustomerReceipts.objects.all()
    serializer_class = serializers.CustomerReceiptsSerializer
