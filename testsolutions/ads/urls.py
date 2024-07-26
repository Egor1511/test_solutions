from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AdViewSet, AddAdsView

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ad')

urlpatterns = router.urls

urlpatterns += [
    path('add_ads/', AddAdsView.as_view(), name='add_ads')
]
