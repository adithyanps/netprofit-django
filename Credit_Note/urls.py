from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CreditNoteViewSet    )

router = DefaultRouter()

router.register('creditnote', CreditNoteViewSet)

app_name = 'credit_note'
urlpatterns = [
    path('',include(router.urls)),
]
