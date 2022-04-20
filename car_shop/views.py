from django.shortcuts import render
from rest_framework import generics
from .models import Mark, Model
from .serailizers import MarkSerializer, ModelSerializer

# Create your views here.


class CreateMark(generics.CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class ListMark(generics.ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class DetailMark(generics.RetrieveAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class CreateModel(generics.CreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ListModel(generics.ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class DetailModel(generics.RetrieveAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    