from django.db import models
import datetime

class Site(models.Model):
	name = models.CharField(max_length=255, null=False)

	def __unicode__(self):
		return self.name

class SiteURL(models.Model):
	url = models.CharField(max_length=255, null=False, unique=True)
	site = models.ForeignKey('Site', null=False)

	def __unicode__(self):
		return self.url

class Click(models.Model):
	x = models.IntegerField(null=False)
	y = models.IntegerField(null=False)
	link = models.CharField(max_length=255, null=True)
	timestamp = models.DateTimeField(default=datetime.datetime.now)

	siteurl = models.ForeignKey('SiteURL', null=False)
