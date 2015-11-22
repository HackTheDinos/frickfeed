from django.db import models

class HasTimestampModel(models.Model):
    """
    Abstract model with timestamp fields
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        abstract = True

class Record(HasTimestampModel):
    '''
    Represents a record or a page in the frick collection
    '''

    frick_n_location = models.CharField()
    frick_n_box = models.IntegerField()

    shipping_point = models.CharField() # or break into city, state
    collector_name_first = models.CharField(max_length=50)
    collector_name_last = models.CharField(max_length=50)
    date_recorded = models.DateField()
    date = models.DateField()
    season_at = models.CharField()

    class Meta:
        db_table = 'record'
        unique_together = ('frick_n_location','frick_n_box')

    def __unicode__(self):
        return u'{}-{}'.(self.frick_n_location, self.frick_n_box


class Specimen(HasTimestampModel):
    '''
    Represents a line on a record
    '''

    record = models.ForeignKey('Record', related_name='specimen')

    field_no = models.IntegerField(blank=False)

    #EG FAM 42326
    amnh_catalog_a = models.CharField(max_length=10) # where does this come from?
    amnh_catalog_b = models.CharField(max_length=10) # where does this come from?

    frick_n_specimen = models.IntegerField()
    description = models.CharField(max_length=200) # or break this up into the components by semicolon?
    location = models.CharField(null=True)

    class Meta:
        db_table = 'specimen'
        unique_together = ('record', 'frick_n_specimen')

    def __unicode__(self):
        return u'{}-{}'.(self.record, self.frick_n_specimen)
