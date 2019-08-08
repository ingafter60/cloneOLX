from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):

	## Each product has its own condition (new and used)
	CONDITION_TYPE = (
		("New", "New"),
		("Used", "Used")
	)

	## It contains all the products information
	name 				= models.CharField(max_length=100)
	owner 			= models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=500)
	condition 	= models.CharField(max_length=100, choices=CONDITION_TYPE)
	price 			= models.DecimalField(max_digits=10, decimal_places=2)
	created 		= models.DateTimeField(default=timezone.now)

	# To change the display from "Product object(1)" to "name"
	def __str__(self):
		return self.name