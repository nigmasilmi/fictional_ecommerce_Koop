# Generated by Django 2.2 on 2019-05-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_auto_20190529_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('electronics', 'Electrónicos'), ('sports', 'Deportes'), ('other', 'Misceláneos')], default='Deportes', max_length=50),
        ),
    ]