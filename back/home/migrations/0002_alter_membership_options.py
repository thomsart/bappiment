# Generated by Django 4.1.7 on 2023-04-28 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membership',
            options={'ordering': ['status', 'user']},
        ),
    ]
