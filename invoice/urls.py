from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            CustomerViewset,
            BranchViewset,ItemViewset,
            C_InvoiceViewset,P_InvoiceViewset,
            AccountViewset,JournalItemViewset,
            JournalEntryViewset,
            ParentInvoiceViewSet,ChildInvoiceViewset,
            AccountDefaultViewSet,CustomerReceiptViewSet,
            ExpenseCategoryViewSet,ExpenseViewSet,
            )

router = DefaultRouter()
router.register('customer', CustomerViewset)
router.register('branch', BranchViewset)
router.register('item', ItemViewset)
router.register('childitemold', C_InvoiceViewset)
router.register('parantdataold', P_InvoiceViewset)
router.register('account', AccountViewset)
router.register('journalitem', JournalItemViewset)
router.register('journalentry', JournalEntryViewset)
router.register('customerReceipt', CustomerReceiptViewSet)
router.register('parantdata', ParentInvoiceViewSet)
router.register('childitem', ChildInvoiceViewset)
router.register('accountDefault', AccountDefaultViewSet)
router.register('expense-category', ExpenseCategoryViewSet)
router.register('expenses', ExpenseViewSet)


app_name = 'invoice'
urlpatterns = [
    path('',include(router.urls)),

]
