# Generated by Django 3.1.2 on 2020-11-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Type',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
    ]