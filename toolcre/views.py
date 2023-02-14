from django.shortcuts import render,redirect


import sqlite3
# Create your views here.

def numb(request):  
    if request.method=="GET":
        return render(request,'templates/form-layouts-vertical.html') 

def num(request):
    if request.method=="GET":
        return render(request,'templates/num.html')
    
def ico(request):
    if request.method=="GET":
        return render(request,'templates/ico.html')
    
  