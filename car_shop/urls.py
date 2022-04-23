from .views import MarkViewSet, ModelViewSet, CategoryViewSet, PartViewSet, PartCodeFilter, PartPriceFilter, \
    MarkNameFilter, ModelNameFilter, CategoryFilter
from rest_framework.routers import SimpleRouter
from django.urls import path


router = SimpleRouter()
router.register('marks', MarkViewSet, basename='marks')
router.register('models', ModelViewSet, basename='models')
router.register('category', CategoryViewSet, basename='category')
router.register('parts', PartViewSet, basename='parts')

urlpatterns = [
               path('parts/<code>/', PartCodeFilter.as_view()),
               path('parts/range/<from>:<to>/', PartPriceFilter.as_view()),
               path('marks/filter/<name>/', MarkNameFilter.as_view()),
               path('models/filter/<model>/', ModelNameFilter.as_view()),
               path('category/filter/<category>', CategoryFilter.as_view()),
               ]

urlpatterns += router.urls
