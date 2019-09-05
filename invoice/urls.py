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
            SalesPartnerChartViewset,SalesYearIncomeChartViewset,
            Sales_PartnerWithYear_ChartViewSet,
            ExpenseYearIncomeChartViewset,Expense_Cat_Vers_Year_AmountChartViewset,
            Expense_Year_Vers_AmountChartViewset
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
router.register('sales-PartnerWithYear-chart', Sales_PartnerWithYear_ChartViewSet,base_name='Sales_PartnerWithYearChart')
router.register('expense-year-chart', ExpenseYearIncomeChartViewset,base_name='expense-year-chart')
router.register('expenseCat-year-amount-chart', Expense_Cat_Vers_Year_AmountChartViewset,base_name='expenseCat-year-amount-chart')
router.register('expenseCat-amount-chart', Expense_Year_Vers_AmountChartViewset,base_name='expenseCat-amount-chart')

app_name = 'invoice'
urlpatterns = [
    path('',include(router.urls)),

]
