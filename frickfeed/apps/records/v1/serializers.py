from apps.records.models import Record, Specimen
from rest_framework.serializers import ModelSerializer


class RecordSerializer(ModelSerializer):
    
    class Meta:
        model = Record


class Specimen(ModelSerializer):

    class Meta:
        model = Specimen
