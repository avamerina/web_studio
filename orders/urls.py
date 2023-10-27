from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet, FileViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')
router.register('files', FileViewSet, basename='files')

urlpatterns = router.urls
