# Generated by Django 4.1.7 on 2023-05-13 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_client_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='user',
            new_name='contact',
        ),
    ]