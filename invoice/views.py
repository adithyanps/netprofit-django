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

class SalesInvoiceViewSetNu(viewsets.ModelViewSet):
    queryset = models.SalesInvoiceNu.objects.all()
    serializer_class = serializers.ParantInvoiceSerializer
    # filter_backends = (DjangoFilterBackend,OrderingFilter, SearchFilter)
    # filter_class = SalesInvoiceFilter
    # search_fields = ('date',"customer")


    def get_queryset(self):
        return self.queryset.order_by('id')


class InvoiceLineOldViewSet(viewsets.ModelViewSet):
    queryset = models.InvoiceLineOld.objects.all()
    serializer_class = serializers.InvoiceLineOldSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
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

class CreditNoteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CreditNoteSerializer
    queryset = models.CreditNote.objects.all()

    def get_queryset(self):
        # Doc_no = self.request.query_params.get('Doc_no')
        # Grand_total = self.request.query_params.get('Grand_total')
        # Date = self.request.query_params.get('Date')
        # Comment = self.request.query_params.get('Comment')
        # print(Doc_no,'jkkkk')
        # print(self.request.query_params,'++++')
        # print(self.request.data,'-----')
        #

        return self.queryset.order_by('id')

    def create(self,request, *args, **kwargs):



        request.data['Doc_no']=105
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        # b = self.number()
        # print(b)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





class CreditNoteNumberViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CreditNoteNumberSerializer
    queryset = models.CreditNoteNumber.objects.all()

#  charts

class SalesPartnerChartViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SalesPartnerChartSerializer
    queryset = models.SalesInvoice.objects.all()

    def list(self, request):
        queryset = models.SalesInvoice.objects.all()

        if queryset:
            dict = {}

            print('wroks')
            for d in queryset.values():
                a,b,c,d,e,f,g,h,i,k,l,m = d.values()
                dict[d] = dict.get(d,0) + l
            user = [{'customer':n,'grant_total':t} for n,t in dict.items()]
            datas= user
            newlist = sorted(datas, key=lambda z: z['customer'])
            # print(newlist,"//")
            queryset = serializers.SalesPartnerChartSerializer(newlist, many=True).data

        return JsonResponse(queryset,safe=False)


class SalesYearIncomeChartViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SalesYearIncomeChartSerializer
    queryset = models.SalesInvoice.objects.all()

    def list(self, request):

        queryset =  models.SalesInvoice.objects.all()
        if queryset:

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
class Sales_PartnerWithYear_ChartViewSet(viewsets.ModelViewSet):
    """get total amount of each person based on every year"""

    queryset =  models.SalesInvoice.objects.all()

    def list(self, request):
        queryset = models.SalesInvoice.objects.all()
        if queryset:

            date_list = []
            name_list = []
            month_list1 = []
            final_list = []
            for d in queryset:
                if d.customer not in name_list:
                    name_list.append(d.customer)
                if d.date.year not in date_list:
                    date_list.append(d.date.year)
            b=[]
            for da in name_list:
                for yr in date_list:
                    month_list = []
                    list = []
                    b = models.SalesInvoice.objects.filter(customer=da, date__year=yr)
                    result = []
                    for i in b:
                        temp = {"month": calendar.month_name[i.date.month], "amount": i.total_amount,"customer":i.customer,"year":i.date.year}
                        month_list.append(temp)
                    month_list1.append(month_list)
            month_list_nu = [x for x in month_list1 if x != []]
            for i in month_list_nu:
                result = defaultdict(int)
                month_sum =[]
                for d in i:
                    result[d['month']] += int(d['amount'])
                    month_sum = [{'month': month, 'amount': amount} for month, amount in result.items()]
                dict = {}
                dict['child'] = month_sum
                for name in i:
                    dict['customer']=name['customer']
                    dict['year']=name['year']
                final_list.append(dict)
            datas =final_list
            print(datas,"???")
        return JsonResponse(datas,safe=False)

class ExpenseYearIncomeChartViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ExpenseYearChartSerializer
    queryset = models.Expenses.objects.all()

    def list(self, request):
        queryset =  models.Expenses.objects.all()
        if queryset:

            date_list = []
            a = []
            b =[]
            amount1 = []
            year = []
            for d in queryset:
                if d.Date.year not in date_list:
                    date_list.append(d.Date.year)
            for da in date_list:
                b = models.Expenses.objects.filter(Date__year=da)
                amount = 0
                for i in b:
                    if i.Date.year == da:
                        amount = i.Amount + amount
                amount1.append(amount)
                year.append(i.Date.year)
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

            queryset = serializers.ExpenseYearChartSerializer(newlist, many=True).data
        return Response(queryset)

class Expense_Cat_Vers_Year_AmountChartViewset(viewsets.ModelViewSet):
    # serializer_class = serializers.ExpenseYearChartSerializer
    queryset = models.Expenses.objects.all()
    def list(self, request):

        queryset = models.Expenses.objects.all()
        if queryset:

            date_list = []
            name_list = []
            month_list1 = []
            final_list = []
            for d in queryset:
                if d.ExpenseCategory.name not in name_list:
                    name_list.append(d.ExpenseCategory.name)
                if d.Date.year not in date_list:
                    date_list.append(d.Date.year)
            b=[]
            for da in name_list:
                for yr in date_list:
                    month_list = []
                    list = []
                    print(yr)
                    b = models.Expenses.objects.filter(ExpenseCategory__name=da,Date__year=yr)
                    result = []
                    for i in b:
                        temp = {"month": calendar.month_name[i.Date.month], "amount": i.Amount,"ExpenseCategory":i.ExpenseCategory.name,"year":i.Date.year}
                        month_list.append(temp)
                    month_list1.append(month_list)
            month_list_nu = [x for x in month_list1 if x != []]
            print(month_list_nu,"=====")
            for i in month_list_nu:
                result = defaultdict(int)
                month_sum =[]
                for d in i:
                    result[d['month']] += int(d['amount'])
                    month_sum = [{'month': month, 'amount': amount} for month, amount in result.items()]
                dict = {}
                dict['child'] = month_sum
                for name in i:
                    dict['ExpenseCategory']=name['ExpenseCategory']
                    dict['year']=name['year']
                final_list.append(dict)
                datas =final_list
        return JsonResponse(datas,safe=False)

class Expense_Year_Vers_AmountChartViewset(viewsets.ModelViewSet):
    queryset = models.Expenses.objects.all()

    if queryset:

        date_list = []
        exCat_list = []
        for d in queryset:
            if d.ExpenseCategory.name not in exCat_list:
                exCat_list.append(d.ExpenseCategory.name)
            if d.Date.year not in date_list:
                date_list.append(d.Date.year)
        print(date_list,"///")
        print(exCat_list,"///")

        for yr in date_list:
            for ex in exCat_list:
                print(ex,yr)

    def list(self, request):
        queryset = models.Expenses.objects.all()
        # data = [{"a":"2"}]

        if queryset:

            data = [{"a":"2"}]
        return JsonResponse({"a":"2"},safe=False)
#
