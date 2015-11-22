from rest_framework.viewsets import ModelViewSet
from apps.records.v1.serializers import RecordSerializer, SpecimenSerializer


class RecordViewSet(ModelViewSet):
    serializer_class = RecordSerializer


class SpecimenViewSet(ModelViewSet):
    serializer_class = SepcimenSerializer
