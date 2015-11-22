from apps.records.models import Record, Specimen
from rest_framework.serializers import ModelSerializer


class RecordSerializer(ModelSerializer):

    class Meta:
        model = Record


class RecordListSerializer(ModelSerializer):

    class Meta:
        model = Record
        fields = [
            'id',
            'location',
            'box',
            'shipping_point',
            'collector_name',
            'date_recorded',
            'date',
            'season_at'
            ]

class SpecimenSerializer(ModelSerializer):

    class Meta:
        model = Specimen
        fields = [
            'record',
            'amnh_catalog_a',
            'amnh_catalog_b',
            'amnh_catalog',
            'frick_number',
            'field_no',
            'description',
            'location'
            ]
