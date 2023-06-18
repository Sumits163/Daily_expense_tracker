from django.shortcuts import render,redirect
from django.contrib import messages
from passlib.hash import django_pbkdf2_sha256 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import *
import traceback


def login(request):
    return render(request,'signin.html',{})

def signup_user(request):
    return render(request, 'signup.html',{})

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        state = request.POST.get('state')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # enpassword = django_pbkdf2_sha256.hash(password)

        if UserRegister.objects.filter(email = email).exists():
            messages.info(request,'Alert:Email already exist!')
            return redirect('/signup/')
        else:
            users = UserRegister()


            
            users.name = name
            users.age = age
            users.gender = gender
            users.state = state
            users.city = city
            users.phone = phone
            users.email = email
            # users.password = enpassword
            users.password=password

            users.save()
            # messages.info(request,'Successfully registerd!')
            return render(request, 'signin.html', {})

            # return redirect('/')
    return render(request, 'signup.html',{})

# def signin_user(request):
#     try:
#         if request.method == 'POST':
#             email = request.POST.get('email')
#             password = request.POST.get('password')

#             user = UserRegister.objects.filter(email = email)
#             if user == None:
#                 messages.error(request,'User Not exist')
#                 return redirect('/')
#             # enpassword = user[0].password
            
#             # if django_pbkdf2_sha256.verify(password,enpassword):
#             users = authenticate(request, username=email, password=password)
#             print(users)
#             if users is not None:
#                 auth_login(request, users)
#                 return render(request,'home.html',{})
            
#             # else:
#             #     messages.error(request,'Alert:Wrong password')
#             #     return  redirect('/')
#         else:
#             messages.error(request,'Alert:Wrong password')
#             return redirect('/')
#     except:
#         traceback.print_exc()
#         return redirect('/')

def signin_user(request):
    try:
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']

            users = UserRegister.objects.filter(email = username).first()
            print(users)
            if users == None:
                messages.error(request,'alert: User not exist')
                return redirect('/')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                auth_login(request,user)
                return render(request,'home.html',{})
            else:
                messages.error(request, 'Username or password is incorrect!')
                return redirect('/')
        else:
    
            return redirect('/')
    except:
        traceback.print_exc()
        return redirect('/')
        
