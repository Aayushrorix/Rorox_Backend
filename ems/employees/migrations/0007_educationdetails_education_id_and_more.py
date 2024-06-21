# Generated by Django 5.0.6 on 2024-06-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_alter_employee_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationdetails',
            name='education_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='experiencedetails',
            name='experience_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
