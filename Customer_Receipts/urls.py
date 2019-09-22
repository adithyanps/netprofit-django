from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerReceiptViewSet
            )

router = DefaultRouter()

router.register('customerReceipt', CustomerReceiptViewSet)

app_name = 'customer_reciepts'
urlpatterns = [
    path('',include(router.urls)),

]
