from rest_framework import routers
from apps.records.v1.viewsets import RecordViewSet, SpecimenViewSet


router = routers.DefaultRouter()
router.register(r'records', RecordViewSet)
router.register(r'specimen', SpecimenViewSet)
router.register(r'specimens', SpecimenViewSet)
