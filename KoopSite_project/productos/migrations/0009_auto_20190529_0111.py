# Generated by Django 2.2 on 2019-05-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_auto_20190529_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Electronicos', 'Electrónicos'), ('Deportes', 'Deportes'), ('Misceláneos', 'Misceláneos')], default='Misceláneos', max_length=50),
        ),
    ]
