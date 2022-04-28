from django.db import models

class Methodologies(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	dateadded = models.DateTimeField(blank=True, null=True)
