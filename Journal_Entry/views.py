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
from Journal_Entry import models
from Journal_Entry import serializers
# from . import Permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters import FilterSet
import django_filters
from django_filters import rest_framework as filters
import calendar



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
