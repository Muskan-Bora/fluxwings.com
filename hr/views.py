from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cust_services, cust_contact
from .forms import contactform
from django.contrib import messages
from hr.models import aboutus, services, why_choose_us

# Create your views here.

def index(request):
    
    ABOUTUS = aboutus.objects.all()
    SERVICES = services.objects.all()
    WHYCHOOSEUS = why_choose_us.objects.all()
    
    if request.method == 'POST':
        form = contactform(request.POST or None)
        if form.is_valid():
            cust_name = form.cleaned_data['cust_name']
            email_id = form.cleaned_data['email_id']
            mobile_no = form.cleaned_data['mobile_no']
            whatsapp_no = form.cleaned_data['whatsapp_no']
            services_required = form.cleaned_data['services_required']
            query = form.cleaned_data['query']
                
            contact_cust = cust_contact.objects.create(
                cust_name = cust_name,
                email_id = email_id,
                mobile_no = mobile_no,
                whatsapp_no = whatsapp_no,
                services_required = services_required,
                query = query,
            )
            messages.success(
                request,
                'Thank You!.. We will contact you Soon..'
            )
                
            return redirect('index')
        
    else:
        form = contactform()
    
    context = {
        'form':form,
        'ABOUTUS':ABOUTUS,
        'SERVICES':SERVICES,
        'WHYCHOOSEUS':WHYCHOOSEUS,
    }
    
    return render(request, 'fluxwings/index.html', context)

def details_services(request, services_id):
    
    detailservices = services.objects.get(id=services_id)
    
    context = {
        'detailservices':detailservices
    }
    
    return render(request, 'fluxwings/details_services.html', context)

def contact(request):
    
    if request.method == 'POST':
        form = contactform(request.POST or None)
        if form.is_valid():
            cust_name = form.cleaned_data['cust_name']
            email_id = form.cleaned_data['email_id']
            mobile_no = form.cleaned_data['mobile_no']
            whatsapp_no = form.cleaned_data['whatsapp_no']
            services_required = form.cleaned_data['services_required']
            query = form.cleaned_data['query']
                
            contact_cust = cust_contact.objects.create(
                cust_name = cust_name,
                email_id = email_id,
                mobile_no = mobile_no,
                whatsapp_no = whatsapp_no,
                services_required = services_required,
                query = query,
            )
            messages.success(
                request,
                'Thank You!.. We will contact you Soon..'
            )
                
            return redirect('index')
        
    else:
        form = contactform()
        
    context = {
        'form':form
    }
    
    return render(request, 'fluxwings/contact.html', context)

def service(request):
    
    SERVICES = services.objects.all()
    
    context = {
        'SERVICES':SERVICES,
    }
    
    return render (request,'fluxwings/service.html', context)

def about_us(request):
    
    ABOUTUS = aboutus.objects.all()
    
    context = {
        'ABOUTUS':ABOUTUS,
    }
    
    return render (request,'fluxwings/aboutus.html', context)
