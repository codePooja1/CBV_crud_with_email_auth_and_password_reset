from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowView.as_view(), name="homepage"),
    path('create/', AddView.as_view(), name="createpage"),
    path('update/<int:i>/', UpdateView.as_view(), name='updatepage'),
    path('delete/<int:i>/', DeleteView.as_view(), name='deletepage')

]
