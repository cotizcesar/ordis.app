# Generated by Django 2.1 on 2018-09-07 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0021_auto_20180906_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='weapon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='codex.Weapon'),
        ),
    ]