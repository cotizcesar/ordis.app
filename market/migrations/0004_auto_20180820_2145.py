# Generated by Django 2.1 on 2018-08-21 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_remove_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='component',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Item'),
        ),
    ]