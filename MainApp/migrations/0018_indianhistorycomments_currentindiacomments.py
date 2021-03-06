# Generated by Django 4.0.4 on 2022-06-15 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0017_alter_currentindianmodel_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndianHistoryComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indianhistorycomments', to='MainApp.indianhistorymodel')),
            ],
            options={
                'verbose_name_plural': 'IndianHistroyComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='CurrentIndiaComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currentindiacomments', to='MainApp.currentindianmodel')),
            ],
            options={
                'verbose_name_plural': 'CurrentIndiaComments',
            },
            bases=('MainApp.comments',),
        ),
    ]
