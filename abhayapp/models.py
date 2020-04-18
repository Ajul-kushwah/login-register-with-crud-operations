from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    address=models.CharField(max_length=200, default="")

    def __str__(self):
        return self.firstname+" "+self.lastname


class TribalYouth(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    username = models.CharField(max_length=50, default='')

    firstname = models.CharField(max_length=50, default='')
    lastname = models.CharField(max_length=50, default='')
    age=models.IntegerField(default=0)
    email = models.EmailField(max_length=50, default='')

    mobile = models.CharField(max_length=10, default='')
    state = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')

    address = models.TextField()

    category = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.username)

class Company(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company_username = models.CharField(max_length=50, default='')
    company_type=models.CharField(max_length=20,default='')
    company_email = models.EmailField(max_length=50, default='')

    category = models.CharField(max_length=20, default='company-user')

    def __str__(self):
        return str(self.company_username)
