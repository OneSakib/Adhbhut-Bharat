# Generated by Django 4.0.4 on 2022-05-31 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_comments_indianhistorycomments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
