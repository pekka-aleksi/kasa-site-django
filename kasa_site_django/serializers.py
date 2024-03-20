import rest_framework.serializers
import kasa_site_django.models


class MyBaseSerializer(rest_framework.serializers.ModelSerializer):
    pass


class LinkSerializer(MyBaseSerializer):
    class Meta:
        fields = ['href', 'text', 'date', 'description']
        model = kasa_site_django.models.Link


class TILSerializer(MyBaseSerializer):

    html = rest_framework.serializers.SerializerMethodField()
    text = rest_framework.serializers.SerializerMethodField()

    def get_html(self, instance):
        return instance.content.html

    def get_text(self, instance):
        return instance.content.plain


    class Meta:
        fields = ['html', 'text']
        model = kasa_site_django.models.TIL