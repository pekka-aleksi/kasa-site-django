from rest_framework.viewsets import ReadOnlyModelViewSet
import rest_framework.response
import kasa_site_django.serializers
import kasa_site_django.models


class LinkViewSet(ReadOnlyModelViewSet):
    queryset = kasa_site_django.models.Link.objects.all()
    serializer_class = kasa_site_django.serializers.LinkSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        retval = rest_framework.response.Response(serializer.data)
        return retval
