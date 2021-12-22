from django.shortcuts import render, redirect
from .models import Laptop
from .forms import LaptopModelForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class AddView(LoginRequiredMixin, View):
    def get(self, request):
        form = LaptopModelForm()
        return render(request, template_name='LaptopApp/form.html', context={'form': form})

    def post(self, request):
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')


class ShowView(View):
    def get(self, request):
        laptops = Laptop.objects.all()
        return render(request, template_name='LaptopApp/home.html', context={'laptops': laptops})


class DeleteView(LoginRequiredMixin, View):
    def get(self, request, i):
        laptop = Laptop.objects.get(id=i)
        return render(request, template_name='LaptopApp/deletepage.html', context={'laptop': laptop})

    def post(self, request, i):
        laptop = Laptop.objects.get(id=i)
        laptop.delete()
        return redirect('homepage')


class UpdateView(LoginRequiredMixin, View):
    def get(self, request, i):
        laptop = Laptop.objects.get(id=i)
        form = LaptopModelForm(instance=laptop)
        return render(request, template_name='LaptopApp/form.html', context={'form': form})

    def post(self, request, i):
        laptop = Laptop.objects.get(id=i)
        form = LaptopModelForm(request.POST, instance=laptop)
        form.save()
        return redirect('homepage')
