from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
            CustomerViewset,
            BranchViewset,ItemViewset,
            C_InvoiceViewset,P_InvoiceViewset
            )
router = DefaultRouter()
router.register('customer', CustomerViewset)
router.register('branch', BranchViewset)
router.register('item', ItemViewset)
router.register('childitem', C_InvoiceViewset)
router.register('parantdata', P_InvoiceViewset)


app_name = 'invoice'

urlpatterns = [

    path('',include(router.urls)),

]
