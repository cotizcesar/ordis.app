# Generated by Django 2.1 on 2018-09-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0017_auto_20180906_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='is_tradeable',
            field=models.BooleanField(default=False),
        ),
    ]