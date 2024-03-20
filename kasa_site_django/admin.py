import django.contrib.admin
import kasa_site_django.models


@django.contrib.admin.register(kasa_site_django.models.TIL)
class TILAdmin(django.contrib.admin.ModelAdmin):
    pass
