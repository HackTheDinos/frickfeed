from apps.records.models import Record, Specimen
from rest_framework.serializers import ModelSerializer


class RecordSerializer(ModelSerializer):
    
    class Meta:
        model = Record


class SpecimenSerializer(ModelSerializer):

    class Meta:
        model = Specimen
