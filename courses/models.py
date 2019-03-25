from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):

	class Meta:
		db_table = "courses"

	# main fields
	title = models.CharField(max_length=128)
	subtitle = models.CharField(max_length=128)
	description = models.TextField(blank=True, default="")
	video_url = models.CharField(max_length=128)
	price = models.FloatField(default=0)
	image_url = models.CharField(max_length=128, null=True, blank=True)

	# relations fields
	created_by = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		null=True
	)

	def __str__(self):
		return self.title