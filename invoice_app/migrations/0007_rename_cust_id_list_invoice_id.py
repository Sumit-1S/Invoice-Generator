# Generated by Django 4.0.3 on 2022-05-23 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0006_remove_list_item_name_remove_list_item_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='cust_id',
            new_name='invoice_id',
        ),
    ]