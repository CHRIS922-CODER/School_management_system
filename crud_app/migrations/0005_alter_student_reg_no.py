# Generated by Django 4.2.1 on 2023-08-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0004_rename_name_course_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]