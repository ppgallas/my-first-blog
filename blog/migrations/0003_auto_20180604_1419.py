# Generated by Django 2.0.5 on 2018-06-04 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180604_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
