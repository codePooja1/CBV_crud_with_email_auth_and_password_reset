from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView

urlpatterns = [
    path('register/', user_register_view, name='registerpage'),
    path('login/', LoginView.as_view(template_name='Users/login1.html'),
         name='loginpage'),
    path('logout/', logout_view, name='logout'),
    path('verify/',verification_view, name='verificationpage'),
    path('reset/',PasswordResetView.as_view(template_name='Users/pswd_reset.html'),name='resetview'),
    path('confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name="Users/mail_sent.html"),name='password_reset_confirm'),
    path('done/',PasswordResetDoneView.as_view(template_name='Users/reset_done.html'),name='password_reset_done'),
    path('complete/',PasswordResetCompleteView.as_view(template_name='Users/done.html'),name='password_reset_complete')
]
