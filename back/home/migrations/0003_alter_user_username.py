# Generated by Django 4.1.7 on 2023-03-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
