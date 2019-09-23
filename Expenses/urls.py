from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            ExpenseCategoryViewSet,
            ExpenseViewSet,
            )

router = DefaultRouter()

router.register('expense-category', ExpenseCategoryViewSet)
router.register('expenses', ExpenseViewSet)




# router.register('sales-partner-chart', SalesPartnerChartViewset,base_name='CustomersYearChart')
# router.register('sales-year-chart', SalesYearIncomeChartViewset,base_name='SalesYearChart')
# router.register('sales-PartnerWithYear-chart', Sales_PartnerWithYear_ChartViewSet,base_name='Sales_PartnerWithYearChart')
# router.register('expense-year-chart', ExpenseYearIncomeChartViewset,base_name='expense-year-chart')
# router.register('expenseCat-year-amount-chart', Expense_Cat_Vers_Year_AmountChartViewset,base_name='expenseCat-year-amount-chart')
# router.register('expenseCat-amount-chart', Expense_Year_Vers_AmountChartViewset,base_name='expenseCat-amount-chart')

app_name = 'expenses'
urlpatterns = [
    path('',include(router.urls)),

]
