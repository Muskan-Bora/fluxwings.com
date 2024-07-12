from django.contrib import admin
from hr.models import cust_contact
from hr.models import cust_services
from hr.models import aboutus
from hr.models import services
from hr.models import why_choose_us

# Register your models here.
admin.site.register(cust_contact)
admin.site.register(cust_services)
admin.site.register(aboutus)
admin.site.register(services)
admin.site.register(why_choose_us)