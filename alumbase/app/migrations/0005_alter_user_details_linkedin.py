# Generated by Django 4.1.5 on 2023-07-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_details_linkedin_alter_interviewexperience_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='linkedin',
            field=models.URLField(max_length=500),
        ),
    ]
