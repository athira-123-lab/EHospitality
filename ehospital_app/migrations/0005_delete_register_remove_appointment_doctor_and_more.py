# Generated by Django 4.2.16 on 2024-09-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehospital_app', '0004_register_patient_age_patient_disease'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.AddField(
            model_name='appointment',
            name='name',
            field=models.CharField(default=1234, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.CharField(null=True),
        ),
    ]
