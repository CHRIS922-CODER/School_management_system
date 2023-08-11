# Generated by Django 4.2.1 on 2023-08-07 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0003_alter_student_course_alter_studentmarks_unit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='studentmarks',
            old_name='unit',
            new_name='unit_code',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='course_id',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='code',
            new_name='unit_code',
        ),
    ]
