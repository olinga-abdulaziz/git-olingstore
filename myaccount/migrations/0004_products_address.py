# Generated by Django 3.2.7 on 2021-10-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0003_products_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='address',
            field=models.CharField(default='Kisumu', max_length=255),
        ),
    ]
