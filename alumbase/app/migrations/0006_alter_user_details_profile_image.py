# Generated by Django 4.1.5 on 2023-07-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_user_details_linkedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='profile_image',
            field=models.ImageField(blank=True, default='https://st3.depositphotos.com/15648834/17930/v/600/depositphotos_179308454-stock-illustration-unknown-person-silhouette-glasses-profile.jpg', null=True, upload_to='profile_images/'),
        ),
    ]
