from django.db import models
from django import forms
from django.core import validators
# Create your models here.

#  built in validation
def startwith_capital(value):
    if value[0].islower():      
       raise forms.ValidationError('start with capital letter')

class Student(models.Model):
    name  = models.CharField(max_length=250,validators=[startwith_capital,                            
                            validators.MaxLengthValidator(10),
                            validators.MinLengthValidator(3)])
    email = models.EmailField(max_length=250)
    phno = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Employee(models.Model) :
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


    def __str__(self):
        return self.name



