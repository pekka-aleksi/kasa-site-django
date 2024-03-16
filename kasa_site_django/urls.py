from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from kasa_site_django import views


router = SimpleRouter()
router.register(r'links', views.LinkViewSet, basename='link')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/admin/', admin.site.urls),
]
