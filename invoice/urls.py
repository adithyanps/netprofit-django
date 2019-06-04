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
            ReceiptView,
            # JournalITEMViewset,JournalEntriesviewset,
            # CustomerReceiptsViewSet
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

# router.register('JournalITEM', JournalITEMViewset)
# router.register('JournalENTRY', JournalEntriesviewset)
# router.register('customerRECIEPT', CustomerReceiptsViewSet)


app_name = 'invoice'
urlpatterns = [
    path('',include(router.urls)),
    # path('parantdata/',Sample.as_view()),
    # path('ReceiptView/',ReceiptView.as_view()),


]
