from django.db import models

# Create your models here.
class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True)
    ph = models.CharField(max_length=45)
    turbidity = models.CharField(max_length=45)
    temperature = models.CharField(max_length=45)

    class Meta:

        db_table = 'reading'
