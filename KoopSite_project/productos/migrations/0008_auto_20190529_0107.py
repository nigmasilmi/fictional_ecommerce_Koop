# Generated by Django 2.2 on 2019-05-29 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20190528_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=10.99),
        ),
    ]