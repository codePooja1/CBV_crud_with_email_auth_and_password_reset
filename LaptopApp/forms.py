from django import forms
from .models import Laptop


class LaptopModelForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Laptop
        labels = {
            'ram': 'RAM',
            'rom': 'ROM'
        }
        widgets = {
            'company': forms.TextInput(attrs={'placeholder': 'eg. Lenovo, Apple'}),
            'model_name': forms.TextInput(attrs={'placeholder': 'eg. ThinkPad, Macbook'}),
            'Processor': forms.TextInput(attrs={'placeholder': 'eg. intel i5 11th gen, AMD Ryzen 5 5500u '}),
            'ram': forms.TextInput(attrs={'placeholder': 'eg. 4GB, 8GB'}),
            'price': forms.TextInput(attrs={'placeholder': 'in Rs.'}),
            'rom': forms.TextInput(attrs={'placeholder': 'eg. 256GB, 512GB'}),
            'weight': forms.TextInput(attrs={'placeholder': 'eg.1.5Kg'})
        }

    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram <= 0:
            raise forms.ValidationError('RAM should be greater than 0')
        else:
            return ram

    def clean_rom(self):
        rom = self.cleaned_data['rom']
        if rom < 64:
            raise forms.ValidationError('ROM must be greater than 64GB')
        else:
            return rom

    def clean_weight(self):
        w = self.cleaned_data['weight']
        if w <= 1 or w >= 4:
            raise forms.ValidationError("Weight cannot be less than 1Kg or greater than 4kg")
        else:
            return w

    def clean_price(self):
        p = self.cleaned_data['price']
        if p <= 10000:
            raise forms.ValidationError("Please enter valid Price")
        else:
            return p
