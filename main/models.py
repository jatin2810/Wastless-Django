from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY = (
('book','book'),
('electronic','electronic'),
('furniture','furniture'),
('clothing','clothing'),
('sport','sport'),
('stationary','stationary'),
('daily_use','daily_use'),
('other','other')
)

class Product(models.Model):   #model for the goods user post on our website
	seller = models.ForeignKey(User,on_delete=models.CASCADE)
	phone_number=models.IntegerField()
	name = models.CharField(max_length=20)
	price = models.IntegerField()
	description = models.CharField(max_length=200)
	image1 = models.ImageField(upload_to='product_image1',blank=True)
	image2 = models.ImageField(upload_to='product_image2',blank=True)
	image3 = models.ImageField(upload_to='product_image3',blank=True)
	category = models.CharField(max_length=30,choices=CATEGORY,default='book')
	address = models.CharField(max_length=100)




	def __str__(self):
		return self.name

NGO_NAME = (
('Prayaas','Prayaas'),
('Pahal','Pahal'),
('NGO1','NGO1'),
('NGO2','NGO2'),
)

class Donate(models.Model):  #model for donation of NGO
	donator = models.ForeignKey(User,on_delete=models.CASCADE)
	phone_number=models.IntegerField()
	quantity = models.CharField(max_length=300)
	description = models.CharField(max_length=200)
	image1 = models.ImageField(upload_to='product_image1',blank=True)
	image2 = models.ImageField(upload_to='product_image2',blank=True)
	image3 = models.ImageField(upload_to='product_image3',blank=True)
	NGO = models.CharField(max_length=30,choices=NGO_NAME,default='Prayaas')
	category = models.CharField(max_length=30,choices=CATEGORY,default='stationary',null=True)
	address = models.CharField(max_length=100)




	def __str__(self):
		return self.donator.username

BLOOD_GROUP =(
	('A+','A+'),
	('A-','A-'),
	('AB+','AB+'),
	('AB-','AB-'),
	('O+','O+'),
	('O-','O-')
)

# class Blood(models.Model):    #model for blood donation data
# 	donator = models.ForeignKey(User,on_delete=models.cascade)
# 	phone_number=models.IntegerField()
# 	blood_group=models.CharField(max_length=10,choices=BLOOD_GROUP)
# 	address = models.CharField(max_length=100)



# 	def __str__(self):
# 		return self.donator.username + str(self.blood_group)



# class Plasma(models.Model):    #model forplasma donation data
# 	donator = models.ForeignKey(User,on_delete=models.cascade)
# 	phone_number=models.IntegerField()
# 	blood_group=models.CharField(max_length=10,choices=BLOOD_GROUP)
# 	address = models.CharField(max_length=100)



# 	def __str__(self):
# 		return self.donator.username + str(self.blood_group)