import django_filters
from django.db import models
from apps.records.models import Record, Specimen

class RecordFilter(django_filters.FilterSet):
    min_date = django_filters.DateTimeFilter(name='date',lookup_type='gte')
    max_date = django_filters.DateTimeFilter(name='date',lookup_type='lte')
    min_date_recorded = django_filters.DateTimeFilter(name='date_recorded',lookup_type='gte')
    max_date_recorded = django_filters.DateTimeFilter(name='date_recorded',lookup_type='lte')

    filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_type': 'icontains',
            }
        }
    }

    class Meta:
        model = Record
        fields = {
            'shipping_point': ['exact'],
            'collector_name_first': ['exact'],
            'collector_name_last': ['exact'],
            'season_at': ['exact'],
            'date_recorded': ['exact'],
            'date': ['exact'],
        }


class SpecimenFilter(django_filters.FilterSet):
    class Meta:
        model = Specimen
        fields = {
            'description': ['icontains'],
            'location': ['icontains']
        }
