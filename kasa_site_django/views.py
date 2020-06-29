from django.template.response import TemplateResponse
from rest_framework.decorators import api_view


def domath(payload):
    try:
        resp = {"": ""}
        return resp
    except Exception as e:
        print(e)
        return {}


@api_view(['GET'])
def index(request):
    return TemplateResponse(request, 'index.html')
