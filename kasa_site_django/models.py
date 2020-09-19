from django.db import models
from rest_framework.serializers import HyperlinkedModelSerializer



class Link(models.Model):
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.CharField(max_length=10)


class LinkSerializer(HyperlinkedModelSerializer):
    class Meta:
        fields = ['url', 'link', 'date', 'description']
        model = Link