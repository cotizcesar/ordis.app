# Generated by Django 2.1.4 on 2018-12-31 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0067_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codex.Item')),
            ],
        ),
    ]