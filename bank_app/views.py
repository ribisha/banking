from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import *

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if password==password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password)
                user.save()
                print('Registration completed successfully')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('login_user')

    return render(request,'register.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user=auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('newpg')
            else:
                messages.info(request, "Incorrect Password")
        else:
            messages.info(request, 'Invalid,Please create an account')
            return redirect('login_user')
    return render(request,'login.html')

def newpg(request):
    return render(request, 'newpg.html')
def bank_form(request):
    return render(request, 'bank_form.html')
def logout_user(request):
    auth.logout(request)
    return redirect('/')

def bankform(request):
    if request.method=='POST':
        # print("Inside POST block")
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        address=request.POST.get('address')
        district=request.POST.get('district')
        branch=request.POST.get('branch')
      
        materials_list=request.POST.getlist('materials')

       
        materials=', '.join(materials_list)

        customer=Customer.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            address=address,
            district=district,
            branch=branch,
            materials=materials
        )
        customer.save()

        return redirect('success')
    return render(request, 'bank_form.html')

def success(request):

    return render(request,'success.html')

