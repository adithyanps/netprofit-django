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


class ItemViewset(viewsets.ModelViewSet):
    """create a new item and see all items"""
    queryset = models.Product.objects.all()
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


class InvoiceLineViewSet(viewsets.ModelViewSet):
    queryset = models.InvoiceLine.objects.all()
    serializer_class = serializers.InvoiceLineSerializer

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

#  charts

class SalesPartnerChartViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SalesPartnerChartSerializer
    queryset = models.SalesInvoice.objects.all()

    dict = {}
    for d in queryset.values():
        a,b,c,d,e,f,g,h,i,k,l,m = d.values()
        dict[d] = dict.get(d,0) + l
    user = [{'customer':n,'grant_total':t} for n,t in dict.items()]
    datas= user
    newlist = sorted(datas, key=lambda z: z['customer'])
    queryset = serializers.SalesPartnerChartSerializer(newlist, many=True).data

class SalesYearIncomeChartViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SalesYearIncomeChartSerializer
    queryset = models.SalesInvoice.objects.all()

    def list(self, request):
        queryset =  models.SalesInvoice.objects.all()
        date_list = []
        a = []
        b =[]
        amount1 = []
        year = []
        for d in queryset:
            if d.date.year not in date_list:
                date_list.append(d.date.year)
        for da in date_list:
            b = models.SalesInvoice.objects.filter(date__year=da)
            amount = 0
            for i in b:
                if i.date.year == da:
                    amount = i.grant_total + amount
            amount1.append(amount)
            year.append(i.date.year)
        list = []
        final_list = []
        for (a,b) in zip(year,amount1):
            templist = []
            templist.append(a)
            templist.append(b)
            list.append(templist)
        list2 = ['year','grant_total']
        for i in list:
            temp_dict = dict(zip(list2,i))
            final_list.append(temp_dict)
        datas = final_list
        newlist = sorted(datas, key=lambda k: k['year'])

        queryset = serializers.SalesYearIncomeChartSerializer(newlist, many=True).data
        return Response(queryset)
