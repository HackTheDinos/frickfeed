from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from apps.records.v1.serializers import RecordSerializer, RecordListSerializer, SpecimenSerializer
from apps.records.v1.filters import RecordFilter, SpecimenFilter
from apps.records.models import Record, Specimen
from rest_framework.response import Response


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_class = RecordFilter

    def list(self, request):
        self.serializer_class = RecordListSerializer
        return super(RecordViewSet, self).list(request)

    def create(self, request):

        field_nos = []

        try:
            data = request.data
            record_data = {
                'location' : data['location'],
                'box' : data['box'],
                'collector_name_first' : data.get('collector_name_first'),
                'collector_name_last' : data.get('collector_name_last'),
                'date_recorded' : data.get('date_recorded'),
                'date' : data.get('date'),
                'season_at' : data.get('season_at')
            }

            obj, created = Record.objects.update_or_create(location=record_data['location'], box=record_data['box'], defaults=record_data)

            record_in_use = obj

        except:
            return Response('Adding record failed.', status=status.HTTP_400_BAD_REQUEST)

        try:
            for specimen in data.get('specimens', []):
                specimen_data = {
                    'amnh_catalog_a' : specimen['amnh_catalog_a'],
                    'amnh_catalog_b' : specimen['amnh_catalog_b'],
                    'field_no': specimen['field_no'],
                    'description': specimen['description'],
                    'location': specimen.get('location')
                }

                obj, created = Specimen.objects.update_or_create(record=record_in_use, amnh_catalog_a=specimen_data['amnh_catalog_a'], amnh_catalog_b=specimen_data['amnh_catalog_b'], defaults=specimen_data)

                field_nos.append(specimen['field_no'])

        except:
            return Response('Adding specimen failed', status=status.HTTP_400_BAD_REQUEST)

        specimens_on_record = Specimen.objects.filter(record=record_in_use)
        specimens_on_record.exclude(field_no__in=field_nos).delete()

        return Response('Hooray!', status=status.HTTP_200_OK)

class SpecimenViewSet(ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer
    filter_class = SpecimenFilter
