from django.db import models

class Post(models.Model):
	audio = models.FileField(upload_to="")
#	audio = models.FileField()
#	duration = models.FloatField()
	