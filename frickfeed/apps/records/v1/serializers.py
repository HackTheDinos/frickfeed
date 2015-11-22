from apps.records.models import Record, Specimen
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.forms.models import model_to_dict


class RecordSerializer(ModelSerializer):

    specimens = SerializerMethodField()

    def get_specimens(self, obj):
        specimens = [model_to_dict(specimen) for specimen in Specimen.objects.filter(record=obj.id)]

        return specimens

    class Meta:
        model = Record
        fields = [
            'id',
            'location',
            'box',
            'shipping_point',
            'collector_name_first',
            'collector_name_last',
            'date_recorded',
            'date',
            'season_at',
            'transcriber_name',
            'specimens'
            ]


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
            'season_at',
            'transcriber_name'
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
