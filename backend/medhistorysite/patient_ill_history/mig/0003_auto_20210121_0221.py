# Generated by Django 3.1.2 on 2021-01-21 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_ill_history', '0002_auto_20201113_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comorbidity',
            name='idSession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.treatmentsession'),
        ),
    ]
