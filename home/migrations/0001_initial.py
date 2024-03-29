# Generated by Django 5.0.2 on 2024-02-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('stock_status', models.IntegerField(default=0)),
                ('available_stock', models.IntegerField(default=0)),
                ('tags', models.ManyToManyField(blank=True, to='home.tag')),
            ],
        ),
    ]
