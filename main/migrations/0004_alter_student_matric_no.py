# Generated by Django 4.0.3 on 2022-07-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_department_student_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='matric_no',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]