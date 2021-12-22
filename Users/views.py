from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from random import randint

user = None
otp = None


def user_register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            form.save()
            global user
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            global otp
            otp = randint(1000, 9999)
            subject = 'Verify your email'
            message = f'Hi {username}, thank you for showing interest in my website. Here is your otp for email verification {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('verificationpage')
    return render(request, template_name='Users/form.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pswd')
        user1 = authenticate(username=u, password=p)
        print(u,p)
        if user1 is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, template_name='Users/login.html', context={})


def logout_view(request):
    logout(request)
    return redirect('loginpage')


def verification_view(request):
    if request.method == 'POST':
        entered_otp = int(request.POST.get('otp'))
        print(entered_otp,otp)
        print(type(entered_otp),type(otp))
        if entered_otp == otp:
            print('If executed')
            user.is_active = True
            user.save()
            return redirect('loginpage')
        messages.error(request,'Otp does not exist')
    return render(request, template_name='Users/otp_verify.html')
