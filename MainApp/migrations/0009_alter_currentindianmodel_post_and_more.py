# Generated by Django 4.0.4 on 2022-05-31 18:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_remove_currentindianmodel_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentindianmodel',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='customandtraditionmodel',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='factblogmodel',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='freedomfightermodel',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='historicalplacemodel',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='indianhistorymodel',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]