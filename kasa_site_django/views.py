from rest_framework.viewsets import ReadOnlyModelViewSet
import rest_framework.response
from kasa_site_django.models import LinkSerializer, Link

class LinkViewSet(ReadOnlyModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        print(request.META)

        a = {k: v for k, v in request.META.items() if 'HTTP' in k or 'DJANGO' in k or 'REQUEST' in k or 'QUERY' in k or 'REMOTE' in k}

        a.update(serializer.data[0])
        print("listing")
        #print(serializer.data)

        retval = rest_framework.response.Response(a)
        return retval
