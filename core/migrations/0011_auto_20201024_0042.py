# Generated by Django 3.1.2 on 2020-10-24 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201024_0033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comments',
            new_name='comment',
        ),
    ]
