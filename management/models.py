from django.db import models
from django.contrib.auth.models import User
import datetime

class Students(models.Model):
    name          = models.CharField(max_length=50)
    father_name   = models.CharField(max_length=50)
    dob           = models.DateField(max_length=50)
    address       = models.TextField()
    city          = models.CharField(max_length=100)
    state         = models.CharField(max_length=100)
    pin           = models.IntegerField()
    phone_no      = models.CharField(max_length=12, unique=True)
    email         = models.EmailField(max_length=100, unique=True)
    class_opted   = models.IntegerField()
    marks         = models.IntegerField()
    date_enrolled = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
