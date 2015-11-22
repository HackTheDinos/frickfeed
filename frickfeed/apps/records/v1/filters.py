import django_filters
from apps.records.models import Record, Specimen

class RecordFilter(django_filters.FilterSet):
    min_date = django_filters.DateTimeFilter(name='date',lookup_type='gte')
    max_date = django_filters.DateTimeFilter(name='date',lookup_type='lte')
    min_date_recorded = django_filters.DateTimeFilter(name='date_recorded',lookup_type='gte')
    max_date_recorded = django_filters.DateTimeFilter(name='date_recorded',lookup_type='lte')

    class Meta:
        model = Record
        fields = {
            'shipping_point': ['icontains'],
            'collector_name_first': ['icontains'],
            'collector_name_last': ['icontains'],
            'season_at': ['icontains'],
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
