# Generated by Django 3.0.5 on 2020-04-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0005_auto_20200421_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
