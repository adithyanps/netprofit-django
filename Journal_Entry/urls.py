from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            JournalItemViewset,
            JournalEntryViewset,

            )

router = DefaultRouter()

router.register('journalitem', JournalItemViewset)
router.register('journalentry', JournalEntryViewset)

app_name = 'journal_entry'
urlpatterns = [
    path('',include(router.urls)),

]
