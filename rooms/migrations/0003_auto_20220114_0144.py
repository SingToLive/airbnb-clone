# Generated by Django 2.2.5 on 2022-01-13 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20220114_0142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RoomTitle',
            new_name='RoomType',
        ),
    ]
