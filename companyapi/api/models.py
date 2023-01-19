from django.db import models

# Create your models here.

class Company(models.Model):
	Company_id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=50)
	Location = models.CharField(max_length=50)
	About = models.TextField()
	Type = models.CharField(max_length=100, choices=(('IT','IT'),('Non Tech','Non Tech'),('Mobiles','Mobiles')))
	addedDate = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.Name

class Employee(models.Model):
	Empoyee_id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=50)
	Employee_type = models.CharField(max_length=100, choices=(('Developer','Developer'),('Manager','Manager'),('Supervisor','Supervisor')))
	Company_id = models.ForeignKey('Company',on_delete=models.CASCADE)


