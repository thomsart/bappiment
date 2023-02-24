# Generated by Django 4.1.7 on 2023-02-24 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.supplier')),
            ],
        ),
    ]
