from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    #friends = models.ForeignKey(Friend, on_delete=models.CASCADE)


class Friend(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    birthday = models.DateTimeField('Friend Birthday')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    

    