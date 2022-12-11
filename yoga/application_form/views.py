from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
# from django.forms import RegisterForm
# from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required



from .models import  Application_form,Alredy_registered_user,Payment
from django.conf import settings 
from django.core.mail import send_mail 
import string
import random
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def AutoGenerate_OTP():
    #generate a random OTP
    otp_id=''.join(random.choices(string.ascii_uppercase+string.digits,k=6))
    return otp_id

def learndj(request):
    return HttpResponse("Hii I m here")



def application_form(request):
    return render(request,"application_form.html")

def already_registered_user(request):
    return render(request,"already_registered_user.html")



@csrf_exempt
def thank_you(request):
    if request.method=="POST":
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        birth_date=request.POST.get("bdate")
        gender=request.POST.get("gender")
        month=request.POST.get("month")
        year=request.POST.get("year")
        batch_time=request.POST.get("batch_time")
        otp=request.POST.get("otp")
        user=Application_form(first_name=first_name,last_name=last_name,email=email,phone=phone,birth_date=birth_date,geder=gender,payment_month=month,payment_year=year,batch_time=batch_time,Otp=otp)
        user.save()
        print(first_name,last_name,email, phone,birth_date,gender,month,year, batch_time, otp)
    return render(request,"thank_you.html")

@csrf_exempt
def next_month_registration_thank_you(request):
    if request.method=="POST":
        email=request.POST.get("email")
        month=request.POST.get("month")
        year=request.POST.get("year")
        batch_time=request.POST.get("batch_time")
        otp=request.POST.get("otp")
       
        user = Alredy_registered_user(email=email,payment_month=month,payment_year=year,batch_time=batch_time,Otp=otp)
        user.save()
        print(email, month,year,batch_time,otp)
    return render(request,"thank_you.html")



def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print("Hllllllllllllllllllll")
            print(form.cleaned_data['Upi_id'])
            print(form.cleaned_data['payment_Img'])
            otp = AutoGenerate_OTP()
            print(otp)
            qw = Payment(Otp = otp, Upi_id=form.cleaned_data['Upi_id'],payment_Img=form.cleaned_data['payment_Img'])
            qw.save()
            return render(request,'otp.html', {'otp' : otp})
    else:
        form= PaymentForm()
    return render(request,'payment.html', {'form' : form})



def success(request):
	return HttpResponse('successfully uploaded')

