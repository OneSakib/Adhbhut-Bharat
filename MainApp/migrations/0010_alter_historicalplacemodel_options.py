# Generated by Django 4.0.4 on 2022-05-31 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_alter_currentindianmodel_post_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalplacemodel',
            options={'ordering': ['timestamp'], 'verbose_name_plural': 'HistoricalPlaceModel'},
        ),
    ]
