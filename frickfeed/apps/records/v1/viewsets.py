from rest_framework.viewsets import ModelViewSet
from apps.records.v1.serializers import RecordSerializer, SpecimenSerializer
from apps.records.models import Record, Specimen


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class SpecimenViewSet(ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer
