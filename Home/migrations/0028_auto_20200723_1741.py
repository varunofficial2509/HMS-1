# Generated by Django 3.0.8 on 2020-07-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0027_auto_20200723_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='in_datetime',
            field=models.DateTimeField(null=True, verbose_name='yyyy/mm/dd 24:60'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='out_datetime',
            field=models.DateTimeField(null=True, verbose_name='yyyy/mm/dd 24:60'),
        ),
    ]
