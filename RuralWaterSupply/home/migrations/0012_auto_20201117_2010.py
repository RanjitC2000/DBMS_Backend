# Generated by Django 3.1.3 on 2020-11-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='slug',
        ),
        migrations.AddField(
            model_name='community',
            name='subject',
            field=models.CharField(default='hi', max_length=100),
            preserve_default=False,
        ),
    ]
