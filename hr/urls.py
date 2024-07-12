from django.urls import path, include
from hr import views as hr_views
from django.contrib import admin

urlpatterns = [
    path('', hr_views.index, name='index'),
    path('details_services/<int:services_id>/', hr_views.details_services, name='details_services'),
    path('contact/', hr_views.contact, name='contact'),
    path('service/', hr_views.service, name='service'),
    path('about_us/', hr_views.about_us, name='about_us'),
]