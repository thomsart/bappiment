# Generated by Django 4.1.7 on 2023-02-24 22:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('siren', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('siret', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('zip_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('nb_street', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LegalEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('nb_street', models.CharField(max_length=10)),
                ('map', models.ImageField(null=True, upload_to='')),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('date_delivering', models.DateField(default=datetime.date.today)),
                ('maintenance_nb', models.PositiveSmallIntegerField(default=0)),
                ('info', models.TextField(blank=True, default='', max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.client')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='legal_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.legalentity'),
        ),
    ]
