# Generated by Django 3.2 on 2021-04-16 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covaxapp', '0002_auto_20210416_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Vname',
            field=models.CharField(default='NULL', max_length=45),
        ),
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.CharField(default='NULL', max_length=45),
        ),
    ]
