# Generated by Django 4.0.3 on 2022-05-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0018_list_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
