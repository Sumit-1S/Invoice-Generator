# Generated by Django 4.0.3 on 2022-05-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0016_alter_items_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='price_per_unit',
            field=models.IntegerField(default=0),
        ),
    ]
