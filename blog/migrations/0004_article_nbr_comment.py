# Generated by Django 2.0 on 2018-09-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180914_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='nbr_comment',
            field=models.IntegerField(default=0),
        ),
    ]
