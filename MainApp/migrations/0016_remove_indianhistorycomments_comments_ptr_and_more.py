# Generated by Django 4.0.4 on 2022-06-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_rename_slideimgae_slideimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indianhistorycomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='indianhistorycomments',
            name='post',
        ),
        migrations.AddField(
            model_name='currentindianmodel',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customandtraditionmodel',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='factblogmodel',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='freedomfightermodel',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='historicalplacemodel',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='indianhistorymodel',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='CurrentIndiaComments',
        ),
        migrations.DeleteModel(
            name='IndianHistoryComments',
        ),
    ]
