# Generated by Django 3.1.2 on 2020-11-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_checkid'),
        ('product', '0006_auto_20201119_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buy_count',
            field=models.ManyToManyField(related_name='buy_product', to='user.User'),
        ),
        migrations.AlterField(
            model_name='product',
            name='watchlist',
            field=models.ManyToManyField(related_name='watch_product', to='user.User'),
        ),
    ]
