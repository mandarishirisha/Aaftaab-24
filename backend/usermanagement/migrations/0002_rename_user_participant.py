# Generated by Django 4.1.1 on 2022-09-12 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Participant',
        ),
    ]
