# Generated by Django 5.0.6 on 2024-05-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cust_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_cust', models.CharField(default='all services', max_length=500)),
            ],
        ),
    ]
