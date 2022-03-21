# Generated by Django 4.0.3 on 2022-03-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PopularProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=200)),
                ('stars', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type_id', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]