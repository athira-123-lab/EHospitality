# Generated by Django 4.2.16 on 2024-09-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehospital_app', '0005_delete_register_remove_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='prescribtion',
            field=models.CharField(default=1234, max_length=255),
            preserve_default=False,
        ),
    ]
