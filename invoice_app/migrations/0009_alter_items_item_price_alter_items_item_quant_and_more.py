# Generated by Django 4.0.3 on 2022-05-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0008_alter_invoice_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_price',
            field=models.IntegerField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_quant',
            field=models.IntegerField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='list',
            name='item_quant',
            field=models.IntegerField(default='0', max_length=100),
        ),
    ]
