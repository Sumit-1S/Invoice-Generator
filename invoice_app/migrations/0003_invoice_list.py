# Generated by Django 4.0.3 on 2022-05-22 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0002_alter_items_item_price_alter_items_item_quant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('UID', models.UUIDField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=10000)),
                ('address', models.TextField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_code', models.CharField(max_length=4)),
                ('item_name', models.CharField(default='', max_length=1000)),
                ('item_quant', models.CharField(default='0', max_length=100)),
                ('item_price', models.CharField(default='0', max_length=100)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice_app.items')),
            ],
        ),
    ]
