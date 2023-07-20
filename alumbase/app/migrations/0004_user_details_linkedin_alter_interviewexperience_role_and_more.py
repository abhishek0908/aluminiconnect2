# Generated by Django 4.1.5 on 2023-07-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_details_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='linkedin',
            field=models.URLField(default='www.linkedin.com', max_length=500),
        ),
        migrations.AlterField(
            model_name='interviewexperience',
            name='role',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='jobnews',
            name='location',
            field=models.CharField(max_length=30),
        ),
    ]