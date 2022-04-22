from .models import Mark, Model, Category, Part
from .serailizers import MarkSerializer, ModelSerializer, CategorySerializer, PartSerializer
from rest_framework import viewsets
from rest_framework import generics
from django.db.models import Q


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class PartCodeFilter(generics.ListAPIView):

    serializer_class = PartSerializer

    def get_queryset(self):
        code = self.kwargs['code']
        return Part.objects.filter(Q(article=code) | Q(article_second=code))


class PartPriceFilter(generics.ListAPIView):
    serializer_class = PartSerializer

    def get_queryset(self):
        print(self.kwargs)
        price_from = self.kwargs['from']
        price_to = self.kwargs['to']
        return Part.objects.filter(part_price__range=[price_from, price_to])
