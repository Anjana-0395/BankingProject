from django.shortcuts import render
from . models import District,Branch

# Create your views here.
def home(request):
    district_list=District.objects.all()
    return render(request,'index.html',{'d_list':district_list})
def registration(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
