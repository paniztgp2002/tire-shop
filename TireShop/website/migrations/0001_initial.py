# Generated by Django 4.1 on 2023-01-26 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=200)),
                ('paid', models.BooleanField()),
                ('datetime', models.DateField()),
                ('postcode', models.CharField(max_length=20)),
                ('customer_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CartContainsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cart_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField()),
                ('seald', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DealContainsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('deal_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=30)),
                ('seller_id', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('layer', models.IntegerField()),
                ('pattern', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=30)),
                ('seller_id', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('layer', models.IntegerField()),
                ('pattern', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=30)),
                ('seller_id', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
                ('balance', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
