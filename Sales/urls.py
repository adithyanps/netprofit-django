from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            SalesInvoiceViewSet,
            InvoiceLineViewSet,
            )

router = DefaultRouter()

router.register('salesInvoice', SalesInvoiceViewSet)
router.register('invoiceLine', InvoiceLineViewSet)
#



app_name = 'sales'
urlpatterns = [
    path('',include(router.urls)),

]
