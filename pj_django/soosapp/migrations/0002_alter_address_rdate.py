# Generated by Django 3.2.5 on 2022-07-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soosapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='rdate',
            field=models.DateTimeField(),
        ),
    ]
