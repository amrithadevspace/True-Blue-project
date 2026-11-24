from django.db import models
from user_register.models import User
# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=45)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:

        db_table = 'feedback'
