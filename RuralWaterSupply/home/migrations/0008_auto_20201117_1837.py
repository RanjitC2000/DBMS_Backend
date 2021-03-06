# Generated by Django 3.1.3 on 2020-11-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201117_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Project_Scale',
            field=models.CharField(choices=[('large', 'Large Scale'), ('small', 'Small Scale')], default='--Project Scale--', max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='Project_Type',
            field=models.CharField(choices=[('water', 'Water'), ('sanitation', 'Sanitation')], default='--Project Type--', max_length=30),
        ),
    ]
