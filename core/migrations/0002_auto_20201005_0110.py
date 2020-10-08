# Generated by Django 3.1.2 on 2020-10-05 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_alpha_tester',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='platform',
            field=models.CharField(choices=[('PC', 'PC'), ('PS5', 'Playstation 5'), ('PS4', 'Playstation 4'), ('XBS', 'Xbox Series S/X'), ('XB1', 'Xbox One'), ('NSW', 'Nintendo Switch')], default='PC', max_length=3),
        ),
    ]