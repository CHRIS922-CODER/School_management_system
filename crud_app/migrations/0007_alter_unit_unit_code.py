# Generated by Django 4.2.1 on 2023-08-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0006_studentmarks_graded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='unit_code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
