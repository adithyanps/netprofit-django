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
from Credit_Note import models
from Credit_Note import serializers
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
class CreditNoteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CreditNoteSerializer
    queryset = models.CreditNote.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('id')

    def create(self,request, *args, **kwargs):
        print(request.data,"ddata")
        doc = request.data['Doc_no']
        print(doc)
        if doc==None:
            request.data['Doc_no']=Utility.autoCreditNoteNumberGenerator()

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # b = self.number()
        # print(b)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
