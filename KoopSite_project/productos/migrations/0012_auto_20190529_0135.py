# Generated by Django 2.2 on 2019-05-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_auto_20190529_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=10990),
        ),
    ]