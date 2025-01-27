# Generated by Django 5.0.6 on 2024-05-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cust_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(default='Your Name', max_length=100)),
                ('email_id', models.EmailField(default='Email Id', max_length=20)),
                ('mobile_no', models.IntegerField(default='1234567890')),
                ('whatsapp_no', models.IntegerField(default='1234567890')),
                ('services_required', models.CharField(default='services', max_length=100)),
                ('query', models.TextField(default='Your Query')),
            ],
        ),
    ]
