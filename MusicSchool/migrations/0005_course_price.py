# Generated by Django 2.1.dev20180203235110 on 2019-04-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicSchool', '0004_auto_20190402_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Price',
            field=models.IntegerField(default=0),
        ),
    ]
