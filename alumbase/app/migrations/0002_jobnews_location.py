# Generated by Django 4.1.5 on 2023-07-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobnews',
            name='location',
            field=models.CharField(default='Banglore', max_length=30),
        ),
    ]