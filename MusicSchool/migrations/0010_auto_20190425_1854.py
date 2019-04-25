# Generated by Django 2.1.dev20180203235110 on 2019-04-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicSchool', '0009_auto_20190425_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='SSurname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='period',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='TSurname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
