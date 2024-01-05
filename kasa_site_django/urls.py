from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from kasa_site_django import views


router = SimpleRouter()
router.register(r'links', views.LinkViewSet, basename='link')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
