# Generated by Django 2.1 on 2018-09-06 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0013_auto_20180901_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestWalkthrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=5000)),
                ('quest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='codex.Quest')),
            ],
        ),
    ]
