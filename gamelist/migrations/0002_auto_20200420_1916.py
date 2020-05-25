# Generated by Django 3.0.5 on 2020-04-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='players',
            new_name='max_players',
        ),
        migrations.AddField(
            model_name='game',
            name='min_players',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=2),
            preserve_default=False,
        ),
    ]
