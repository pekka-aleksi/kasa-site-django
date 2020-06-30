from django.db import models
from rest_framework import serializers


class LinkSerializer(serializers.Serializer):
    #link_id = serializers.IntegerField()
    url = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)





class Link(models.Model):
    #link_id = models.IntegerField()
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
