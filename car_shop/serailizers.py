from .models import Mark
from rest_framework import serializers


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ('mark_name', 'mark_slug', 'image')
