# Generated by Django 2.1 on 2018-10-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_userprofile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]