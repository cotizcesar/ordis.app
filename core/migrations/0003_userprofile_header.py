# Generated by Django 3.1.2 on 2020-10-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201005_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='header',
            field=models.ImageField(blank=True, default='user/header/default.png', upload_to='user/header'),
        ),
    ]
