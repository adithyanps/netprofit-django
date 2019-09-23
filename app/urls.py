"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from Sales.urls import router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/invoice/', include('invoice.urls')),
    path('api/masters/', include('Masters.urls')),
    path('api/journal_entry/', include('Journal_Entry.urls')),
    path('api/customer_reciepts/', include('Customer_Receipts.urls')),
    path('api/credit_note/', include('Credit_Note.urls')),
    path('api/expenses/', include('Expenses.urls')),
    path('api/sales/', include('Sales.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns
