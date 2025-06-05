from django.shortcuts import render,redirect,HttpResponse
from .forms import  *
from django.views.generic import View
# Create your views here.


class StudentList(View) :
    def get(self,request) :
        sfdo = StudentForm()
        return render(request,'student/home.html',{'sfdo':sfdo})
    def post(self,request):
        sfdo = StudentForm(data= request.POST)
        if sfdo.is_valid():
          sfdo.save() 
          print(sfdo)
          return HttpResponse('done')
        
        return render(request,'student/home.html',{'sfdo':sfdo})
        
        