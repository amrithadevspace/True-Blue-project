from django.db import models


# Create your models here.


class Technecian(models.Model):
    technecian_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    qulification = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:

        db_table = 'technecian'