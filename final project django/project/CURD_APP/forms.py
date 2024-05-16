from django import forms
from .models import Order


pay_list = [('Google Pay', 'Google Pay'), ('Phone Pay', 'Phone Pay'), ('Cash ON Delivery', 'Cash ON Delivery')]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {'oid': 'Order ID ',
                  'prod_name': 'Product',
                  'prod_quan': 'Quantity',
                  'del_date': 'Delivery date',
                  'del_address': 'Delivery Address',
                  'payment_mode': 'Payment',
                 }
        widgets = {'oid': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'e.g.101'}),
                   'prod_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g.Smartphone'}),
                   'prod_quan': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g.1'}),
                   'del_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'del_address': forms.Textarea(attrs={'cols': '30', 'rows': '6', 'class': 'form-control', 'placeholder': 'e.g.Karvenagar, pune'}),
                   'payment_mode': forms.Select(choices=pay_list, attrs={'class': 'form-control'}),
                   }