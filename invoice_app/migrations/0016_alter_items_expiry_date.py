# Generated by Django 4.0.3 on 2022-05-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0015_alter_items_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]
