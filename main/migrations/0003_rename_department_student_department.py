# Generated by Django 4.0.3 on 2022-06-30 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_course_level_alter_course_semester_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Department',
            new_name='department',
        ),
    ]
