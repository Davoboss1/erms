# Generated by Django 4.0.3 on 2022-08-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_student_matric_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(default='Core', max_length=10),
            preserve_default=False,
        ),
    ]
