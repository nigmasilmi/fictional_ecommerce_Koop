# Generated by Django 2.2 on 2019-05-29 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_auto_20190529_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Electronicos', 'Electrónicos'), ('Deportes', 'Deportes'), ('Miscelaneos', 'Misceláneos')], default='Miscelaneos', max_length=50),
        ),
    ]
