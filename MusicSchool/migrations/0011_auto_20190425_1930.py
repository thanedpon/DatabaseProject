# Generated by Django 2.1.dev20180203235110 on 2019-04-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicSchool', '0010_auto_20190425_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='Learn_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teach',
            name='Teach_hour',
            field=models.IntegerField(default=0),
        ),
    ]