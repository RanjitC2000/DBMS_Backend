# Generated by Django 3.1.3 on 2020-11-17 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='TimeSlot',
            field=models.TimeField(),
        ),
    ]