from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            PartnerViewSet,
            BranchViewset,
            ItemViewset,ProductCategoryViewSet,
            AccountViewset,JournalItemViewset,
            JournalEntryViewset,
            ParentInvoiceViewSet,ChildInvoiceViewset,
            AccountDefaultViewSet,CustomerReceiptViewSet,
            ExpenseCategoryViewSet,ExpenseViewSet,
            SalesInvoiceViewSet,
            InvoiceLineViewSet
            )

router = DefaultRouter()
router.register('partner', PartnerViewSet)
router.register('branch', BranchViewset)
router.register('product-category', ProductCategoryViewSet)
router.register('item', ItemViewset)
router.register('parantdata', SalesInvoiceViewSet)
router.register('invoiceLine', InvoiceLineViewSet)
router.register('account', AccountViewset)
router.register('journalitem', JournalItemViewset)
router.register('journalentry', JournalEntryViewset)
router.register('customerReceipt', CustomerReceiptViewSet)
router.register('parantdataold', ParentInvoiceViewSet)
router.register('childitem', ChildInvoiceViewset)
router.register('accountDefault', AccountDefaultViewSet)
router.register('expense-category', ExpenseCategoryViewSet)
router.register('expenses', ExpenseViewSet)

app_name = 'invoice'
urlpatterns = [
    path('',include(router.urls)),

]
