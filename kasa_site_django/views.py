from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from kasa_site_django.models import Link, LinkSerializer

import io


@api_view(['GET'])
def endpoint(request):
    link_objects = Link.objects.all()
    serialized_objects = LinkSerializer(link_objects, many=True)
    data = serialized_objects.data
    rendered_data = JSONRenderer().render(data)
    deserialized_data = JSONParser().parse(io.BytesIO(rendered_data))

    return Response(deserialized_data)
