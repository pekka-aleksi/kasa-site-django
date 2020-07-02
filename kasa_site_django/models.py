from django.db import models
from rest_framework import serializers


class LinkSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    url = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)

    # there's a bug in the sqlite3 DateTimeFields -- they return None
    date = serializers.CharField(max_length=10)  # YYYY-MM-DD


class Link(models.Model):
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.CharField(max_length=10)
