# Generated by Django 2.2 on 2019-05-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20190527_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='koop.jpg', upload_to='images/'),
        ),
    ]