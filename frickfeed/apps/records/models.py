from django.db import models
from django_extensions.db.models import TimeStampedModel


class Record(TimeStampedModel):
    '''
    Represents a record or a page in the frick collection
    '''

    location = models.CharField(max_length=10, null=False, blank=False)
    box = models.IntegerField(null=False, blank=False)

    shipping_point = models.CharField(max_length=100, blank=True, null=True)
    collector_name_first = models.CharField(max_length=50, blank=True, null=True)
    collector_name_last = models.CharField(max_length=50, blank=True, null=True)
    date_recorded = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    season_at = models.CharField(max_length=50, blank=True, null=True)

    transcriber = models.ForeignKey('socialaccount.socialaccount', blank=True, null=True)

    class Meta:
        db_table = 'record'
        unique_together = ('location','box')

    def __unicode__(self):
        return u'{}-{}'.format(self.location, self.box)

    @property
    def collector_name(self):
        return '{}, {}'.format(self.collector_name_last, self.collector_name_first)

    @property
    def transcriber_name(self):
        return u'{}'.format(self.transcriber.extra_data.get('name'))

class Specimen(TimeStampedModel):
    '''
    Represents a line on a record
    '''

    record = models.ForeignKey('Record', related_name='specimen')

    #EG FAM 42326
    amnh_catalog_a = models.CharField(max_length=10) # where does this come from?
    amnh_catalog_b = models.CharField(max_length=10) # where does this come from?

    field_no = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=300) # or break this up into the components by semicolon?
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'specimen'
        unique_together = ('record', 'field_no')

    def __unicode__(self):
        return u'{}-{}'.format(self.record, self.field_no)

    @property
    def amnh_catalog(self):
        return '{} {}'.format(self.amnh_catalog_a, self.amnh_catalog_b)

    @property
    def frick_number(self):
        return '{}-{}-{}'.format(self.record.location, self.record.box, self.field_no)
