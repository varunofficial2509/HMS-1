# Generated by Django 3.0.8 on 2020-07-22 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_auto_20200722_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fathermobileno',
            new_name='father_mobile_no',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='fathername',
            new_name='father_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mobileno',
            new_name='mobile_no',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='rollno',
            new_name='roll_no',
        ),
    ]