# Generated by Django 4.0.3 on 2022-05-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0012_alter_invoice_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='item_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='list',
            name='item_quant',
            field=models.IntegerField(default=0),
        ),
    ]