# Generated by Django 3.1.2 on 2020-10-31 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='def.png', upload_to='')),
            ],
        ),
    ]
