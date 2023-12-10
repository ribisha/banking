from django.db import models
class Bank(models.Model):
    username=models.CharField(max_length=100)


class Customer(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.TextField()
    district=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    materials=models.CharField(max_length=100)
    def __str__(self):
        return self.name





