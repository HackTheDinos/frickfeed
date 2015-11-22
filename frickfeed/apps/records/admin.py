from django.contrib import admin
from apps.records.models import Record, Specimen


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass


@admin.register(Specimen)
class Specimen(admin.ModelAdmin):
    pass
