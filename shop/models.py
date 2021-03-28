from django.db import models
from django.utils import timezone

# Create your models here.
class ProductModel(models.Model):
	name = models.CharField(max_length=100)
	cost = models.CharField(max_length=50)
	image = models.FileField(blank=True, null=True, upload_to='img')
	company = models.CharField(max_length=100)
	color = models.CharField(max_length=50)
	date = models.DateField(default=timezone.now())

	def __str__(self):
		return self.name