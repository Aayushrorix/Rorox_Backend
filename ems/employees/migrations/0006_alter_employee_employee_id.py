# Generated by Django 5.0.6 on 2024-06-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_employee_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
