# Generated by Django 3.0.8 on 2020-07-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0035_appeal_father_mobile_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes'),
        ),
    ]
