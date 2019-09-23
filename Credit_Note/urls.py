from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            CreditNoteViewSet,
            CreditNoteNumberViewSet
            )

router = DefaultRouter()

router.register('creditnote', CreditNoteViewSet)
router.register('creditnote-number', CreditNoteNumberViewSet,base_name='creditnote-number')

app_name = 'credit_note'
urlpatterns = [
    path('',include(router.urls)),
]
