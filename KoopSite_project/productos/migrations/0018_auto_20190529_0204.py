# Generated by Django 2.2 on 2019-05-29 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0017_auto_20190529_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.IntegerField(auto_created=True, unique_for_date='fecha_ingreso'),
        ),
    ]
