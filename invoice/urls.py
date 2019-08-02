from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            PartnerViewSet,
            BranchViewset,AreaViewSet,
            ItemViewset,ProductCategoryViewSet,
            AccountViewset,JournalItemViewset,
            JournalEntryViewset,
            AccountDefaultViewSet,CustomerReceiptViewSet,
            ExpenseCategoryViewSet,ExpenseViewSet,
            SalesInvoiceViewSet,
            InvoiceLineViewSet,
            SalesPartnerChartViewset,SalesYearIncomeChartViewset
            )

router = DefaultRouter()
router.register('partner', PartnerViewSet)
router.register('branch', BranchViewset)
router.register('area', AreaViewSet)
router.register('product-category', ProductCategoryViewSet)
router.register('item', ItemViewset)
router.register('parantdata', SalesInvoiceViewSet)
router.register('invoiceLine', InvoiceLineViewSet)
router.register('account', AccountViewset)
router.register('journalitem', JournalItemViewset)
router.register('journalentry', JournalEntryViewset)
router.register('customerReceipt', CustomerReceiptViewSet)
router.register('accountDefault', AccountDefaultViewSet)
router.register('expense-category', ExpenseCategoryViewSet)
router.register('expenses', ExpenseViewSet)
router.register('sales-partner-chart', SalesPartnerChartViewset,base_name='CustomersYearChart')
router.register('sales-year-chart', SalesYearIncomeChartViewset,base_name='SalesYearChart')

app_name = 'invoice'
urlpatterns = [
    path('',include(router.urls)),

]
