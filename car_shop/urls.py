from .views import MarkViewSet, ModelViewSet, CategoryViewSet, PartViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('marks', MarkViewSet, basename='marks')
router.register('models', ModelViewSet, basename='models')
router.register('category', CategoryViewSet, basename='category')
router.register('parts', PartViewSet, basename='parts')

urlpatterns = router.urls
