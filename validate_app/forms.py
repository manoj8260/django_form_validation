from django import forms
from .models import Student
from django.core import exceptions


# for django form validation
class EmployeeDjangoForm(forms.Form):
    name = forms.CharField(
        max_length=250,error_messages={'required':'name field is required'})
    email = forms.EmailField()
    phno = forms.CharField()


#for modelform validation 

class VAlueIsShort(exceptions.ValidationError) :
    
    def __init__(self, message = None):
         if message is None:
             message = 'length of the value is less than 4 '
         super().__init__(message)    
         




class StudentForm(forms.ModelForm):
    class Meta : 
        model = Student
        fields ='__all__'
        labels = {
            'name': 'Full Name'
        }
        widgets  = {
            'name' :forms.TextInput(attrs={'placeholder' : 'Full Name'}) ,
            'email' :forms.EmailInput(attrs={'class': 'form-control','placeholder':'password'})
        }
        
   
    # def    clean_name(self):
    #      valid_name = self.cleaned_data.get('name')
    #      if len(valid_name) <4 :
    #          raise VAlueIsShort() 
    #      return valid_name
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
       

        if  name in email  :
            raise forms.ValidationError('Name should not be part of the emails')
        
    
       


        



