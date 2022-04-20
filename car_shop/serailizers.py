from .models import Mark, Model, Category
from rest_framework import serializers


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ('mark_name', 'mark_slug', 'image')


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('mark', 'model_name', 'model_slug', 'image')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('model', 'category_name', 'category_slug')