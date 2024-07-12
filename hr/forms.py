from django import forms
from django.forms import ModelForm

from .models import cust_contact
from .models import cust_services

class contactform(forms.Form):
    cust_name = forms.CharField(
        max_length=100,
        label='Required Field', required=True
    )
    
    email_id = forms.EmailField(
        max_length=20,
        label='Required Field', required=True
    )
    
    mobile_no = forms.IntegerField(
        label='Required Field', required=True
    )
    
    whatsapp_no = forms.IntegerField(
        label='Required Field', required=True
    )
    
    services_required = forms.ModelChoiceField(
        queryset=cust_services.objects.all(), empty_label="--- Select Services ---",
        label='Required Field', required=True
    )
    
    query = forms.CharField(widget=forms.Textarea(attrs={'cols':30, 'rows':10, 'style': 'resize:vertical,horizontal', 'placeholder': 'Enter your Query here...',}),
        label='Optional Field', required=False,
    )
    
    class Meta:
        model = cust_contact
        fields = ['cust_name', 'email-id', 'mobile_no', 'whatsapp_no', 'query']