# Generated by Django 3.0.8 on 2020-07-22 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_auto_20200722_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll_no',
            new_name='rollno',
        ),
    ]
