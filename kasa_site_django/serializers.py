import rest_framework.serializers
import kasa_site_django.models


class MyBaseSerializer(rest_framework.serializers.ModelSerializer):
    pass


class LinkSerializer(MyBaseSerializer):
    class Meta:
        fields = ['link', 'date', 'description']
        model = kasa_site_django.models.Link
