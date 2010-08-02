from django.db import models
import datetime

# Create your models here.
class Click(models.Model):
	x = models.IntegerField(null=False)
	y = models.IntegerField(null=False)
	link = models.CharField(max_length=255, null=True)
	timestamp = models.DateTimeField(default=datetime.datetime.now)
