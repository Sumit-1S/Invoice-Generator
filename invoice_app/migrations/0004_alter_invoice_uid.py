# Generated by Django 4.0.3 on 2022-05-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0003_invoice_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='UID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
