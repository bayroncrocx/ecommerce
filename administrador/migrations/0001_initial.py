# Generated by Django 4.0.5 on 2022-12-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporteria',
            fields=[
                ('id_repor', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50)),
                ('product_name', models.CharField(blank=True, max_length=50)),
                ('slug', models.CharField(blank=True, max_length=50)),
                ('accion', models.CharField(blank=True, max_length=50)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]