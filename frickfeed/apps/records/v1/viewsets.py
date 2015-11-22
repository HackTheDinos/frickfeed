from rest_framework.viewsets import ModelViewSet
from apps.records.v1.serializers import RecordSerializer, RecordListSerializer, SpecimenSerializer
from apps.records.v1.filters import RecordFilter, SpecimenFilter
from apps.records.models import Record, Specimen


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_class = RecordFilter

    def list(self, request):
        self.serializer_class = RecordListSerializer
        return super(RecordViewSet, self).list(request)

class SpecimenViewSet(ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer
    filter_class = SpecimenFilter
