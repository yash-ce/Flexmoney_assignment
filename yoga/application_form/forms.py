from django import forms
from .models import *
 
 
class PaymentForm(forms.ModelForm):
 
    class Meta:
        model = Payment
        fields = ['Upi_id', 'payment_Img']