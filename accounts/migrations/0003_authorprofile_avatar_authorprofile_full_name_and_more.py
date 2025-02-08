# Generated by Django 5.1.4 on 2024-12-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_reader'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar_user'),
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='link_facebook',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='link_other',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='link_x',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
