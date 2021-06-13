from django.db import models
from django.contrib.auth.models import User
from datetime import date
#from users.utils.age_validator import MinAgeValidator
import datetime
# Create your models here.
class Students(models.Model):
    name          = models.CharField(max_length=50)
    father_name   = models.CharField(max_length=50)
    dob           = models.DateField(max_length=50)#,validators=[MinAgeValidator(10)])
    address       = models.TextField()
    city          = models.CharField(max_length=100)
    state         = models.CharField(max_length=100)
    pin           = models.IntegerField()
    phone_no      = models.CharField(max_length=12, unique=True)
    email         = models.EmailField(max_length=100, unique=True)
    class_opted   = models.IntegerField()
    marks         = models.IntegerField()
    date_enrolled = models.DateField(default=datetime.datetime.now())

    def clean_date_of_birth(self):
        dob = self.cleaned_data['dob']
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
            return('Must be at least 18 years old to register')
        return dob

    def __str__(self):
        return self.name
