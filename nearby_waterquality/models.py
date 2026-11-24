from django.db import models

# Create your models here.
class NearbyWaterquality(models.Model):
    nearby_waterquality_id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=45)
    ph = models.FloatField()

    class Meta:

        db_table = 'nearby_waterquality'
