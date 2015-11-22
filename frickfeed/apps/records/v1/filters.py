import django_filters
from apps.records import Record, Specimen

class RecordFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = {
            'shipping_point': ['icontains'],
            'collector_name_first': ['icontains'],
            'collector_name_last': ['icontains'],
            'season_at': ['icontains'],
            'date_recorded': ['exact'],
            'date': ['exact']
        }


class SpecimenFilter(django_filters.FilterSet):
	class Meta:
        model = Specimen
        fields = {
        	'description': ['icontains'],
        	'location': ['icontains']
        }
