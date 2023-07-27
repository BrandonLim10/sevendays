# Generated by Django 4.2.3 on 2023-07-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='banner_title',
            field=models.CharField(default='Welcome to my generic page', max_length=100),
        ),
    ]