# Generated by Django 5.0.6 on 2024-05-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0005_why_choose_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust_contact',
            name='email_id',
            field=models.EmailField(default='Email Id', max_length=254),
        ),
    ]