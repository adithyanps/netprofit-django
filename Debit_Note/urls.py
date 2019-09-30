
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (DebitNoteViewSet  )

router = DefaultRouter()

router.register('debitnote', DebitNoteViewSet)

app_name = 'debit_note'
urlpatterns = [
    path('',include(router.urls)),
]
