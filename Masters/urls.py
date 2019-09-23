from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            PartnerViewSet,
            BranchViewset,
            AreaViewSet,
            ProductViewset,
            ProductCategoryViewSet,
            AccountViewset,
            AccountDefaultViewSet,
            )

router = DefaultRouter()
router.register('partner', PartnerViewSet)
router.register('branch', BranchViewset)
router.register('area', AreaViewSet)
router.register('product-category', ProductCategoryViewSet)
router.register('product', ProductViewset)
router.register('account', AccountViewset)
router.register('accountDefault', AccountDefaultViewSet)

app_name = 'masters'
urlpatterns = [
    path('',include(router.urls)),

]
