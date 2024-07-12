from django.db import models

# Create your models here.

class cust_contact(models.Model):
    cust_name = models.CharField(
        max_length=100,
        default='Your Name'
    )
    
    email_id = models.EmailField(
        default='Email Id'
    )
    
    mobile_no = models.IntegerField(
        default='1234567890'
    )
    
    whatsapp_no = models.IntegerField(
        default='1234567890'
    )
    
    services_required = models.CharField(
        max_length=100,
        default='services'
    )
    
    query = models.TextField(
        default='Your Query'
    )
    
    def __str__(self):
        return str(
            (
                self.cust_name,
                self.email_id,
                self.mobile_no,
                self.whatsapp_no,
                self.services_required,
                self.query,
            )
        )
        
class cust_services(models.Model):
    services_cust = models.CharField(
        max_length = 500,
        default='all services'
    )
    
    def __str__(self):
        return self.services_cust
    
class aboutus(models.Model):
    about_feature = models.CharField(
        max_length=100,
        default='about main feature'
    )
    descriptions = models.TextField(
        default='description'
    )
    
    def __str__(self):
        return self.about_feature
    
class services(models.Model):
    service_name = models.CharField(
        max_length=200,
        default='name of services'
    )
    description_services = models.TextField(
        default='description of services'
    )
    
    def __str__(self):
        return self.service_name
    
class why_choose_us(models.Model):
    feature = models.CharField(
        max_length=200,
        default='reason points why choose us'
    )
    description_whychooseus = models.TextField(
        default='description of why choose us'
    )
    
    def __str__(self):
        return self.feature