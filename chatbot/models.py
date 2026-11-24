from django.db import models

# Create your models here.
class Chatbot(models.Model):
    chatbot_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100)

    class Meta:

        db_table = 'chatbot'
