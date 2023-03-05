# Generated by Django 4.1.7 on 2023-03-02 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=50, unique=True)),
                ('dimension', models.JSONField(null=True)),
                ('total_bought', models.PositiveIntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('sale', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('doc', models.FileField(null=True, upload_to='')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.productbrand')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.productfamily')),
            ],
        ),
        migrations.CreateModel(
            name='InstallationProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('installation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.installation')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
            ],
        ),
    ]
