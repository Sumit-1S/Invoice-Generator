# Generated by Django 4.0.3 on 2022-05-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0011_alter_list_invoice_id_alter_list_item_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='UID',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]