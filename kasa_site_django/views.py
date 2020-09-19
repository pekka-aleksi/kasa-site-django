from rest_framework.viewsets import ModelViewSet

from kasa_site_django.models import LinkSerializer, Link


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
