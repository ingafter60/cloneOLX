from django.db import models

# Create your models here.

class Product(models.Model):

	## Each product has its own condition (new and used)
	CONDITION_TYPE = (
		("New", "New"),
		("Used", "Used")
	)

	## It contains all the products information
	name 				= models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	condition 	= models.CharField(max_length=100, choices=CONDITION_TYPE)
	price 			= models.DecimalField(max_digits=10, decimal_places=5)
	created 		= models.DateTimeField()

	# To change the display from "Product object(1)" to "name"
	def __str__(self):
		return self.name