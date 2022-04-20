from django.shortcuts import render
from rest_framework import generics
from .models import Mark
from .serailizers import MarkSerializer

# Create your views here.


class CreateMark(generics.CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class ListMark(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class DetailMark(generics.RetrieveAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer