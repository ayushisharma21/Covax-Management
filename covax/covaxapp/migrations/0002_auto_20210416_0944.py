# Generated by Django 3.2 on 2021-04-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covaxapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Cid',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_id',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
    ]