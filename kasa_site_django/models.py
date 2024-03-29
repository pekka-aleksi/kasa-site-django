import django.db.models
import django.utils.timezone
import django_quill.fields


class MyBaseModel(django.db.models.Model):
    created_at = django.db.models.DateTimeField(default=django.utils.timezone.now)
    updated_at = django.db.models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Link(MyBaseModel):
    href = django.db.models.CharField(max_length=1024)
    text = django.db.models.CharField(max_length=200)
    description = django.db.models.CharField(max_length=1024)
    date = django.db.models.DateTimeField(default=django.utils.timezone.now)


class TIL(MyBaseModel):
    content = django_quill.fields.QuillField()
