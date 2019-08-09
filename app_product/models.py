from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# model name: Product
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
	category 		= models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	brand 			= models.ForeignKey('Brand' , on_delete=models.SET_NULL , null=True)
	price 			= models.DecimalField(max_digits=10, decimal_places=2)
	image 			= models.ImageField(upload_to='main_product/', blank=True, null=True)
	created 		= models.DateTimeField(default=timezone.now)

	# To change the display from "Product object(1)" to "name"
	def __str__(self):
		return self.name

# model name: Category
class Category(models.Model):
	## It contains information about product Category
	category_name 	= models.CharField(max_length=50)
	image 					= models.ImageField(upload_to='category/', blank=True, null=True)

	## Making correct plural of 'Categorys' to 'Categories'
	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.category_name		

# model name: Brand
class Brand(models.Model):
    ## for product brand
    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name		

# model name: Brand
class ProductImages(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    image 	= models.ImageField(upload_to='products/', blank=True , null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'        

    def __str__(self):
        return self.product.name
