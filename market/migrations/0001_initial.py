# Generated by Django 2.1 on 2018-08-21 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('slug', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, default='item/default.png', upload_to='item')),
                ('ducats', models.PositiveIntegerField(blank=True)),
                ('trading_tax', models.PositiveIntegerField()),
                ('mastery_level', models.PositiveIntegerField()),
                ('rarity', models.CharField(choices=[('P', 'Peculiar'), ('C', 'Common'), ('U', 'Uncommon'), ('R', 'Rare'), ('L', 'Legendary'), ('I', 'Riven')], max_length=1)),
                ('mod_rank', models.PositiveIntegerField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Item')),
            ],
        ),
    ]
