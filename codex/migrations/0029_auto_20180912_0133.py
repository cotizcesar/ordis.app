# Generated by Django 2.1 on 2018-09-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0028_auto_20180911_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='image',
            field=models.ImageField(blank=True, default='codex/weapons/default.png', upload_to='codex/weapons'),
        ),
    ]