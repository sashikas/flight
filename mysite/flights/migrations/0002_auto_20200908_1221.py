# Generated by Django 3.1.1 on 2020-09-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
