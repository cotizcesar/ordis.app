# Generated by Django 2.1 on 2018-10-29 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181028_0706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_created']},
        ),
    ]