# Generated by Django 4.0.6 on 2022-07-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soosapp', '0003_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=50)),
                ('rdate', models.DateTimeField()),
                ('udate', models.DateTimeField()),
            ],
        ),
    ]
