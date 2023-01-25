from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from . models import User


# Create your views here.
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,"signup.html")

# create signup form
def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        DOB = request.POST['DOB']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
        elif User.objects.filter(contact=contact).exists():
            messages.error(request,"contact already exists")
        else:
            User.objects.create(name=name,email=email,contact=contact,DOB=DOB,password=password)
        return redirect("/login/")

# create login form
def login_form(request):
    if request.method =='POST':
        contact = request.POST['contact']
        l_password = request.POST['password']
        if User.objects.filter(contact=contact).exists():
           obj = User.objects.get(contact=contact)
           password = obj.password
           if check_password(l_password, password):
                return redirect("/table/")
           else:
            return HttpResponse('password incorrect')
    else:
        return HttpResponse("phone number is not registered")
        
def table(request):
    data = User.objects.all()
    return render(request,'table.html',{"data":data})