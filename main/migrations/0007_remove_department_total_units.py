# Generated by Django 4.0.3 on 2022-08-16 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_department_core_units_department_elective_units_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='total_units',
        ),
    ]
