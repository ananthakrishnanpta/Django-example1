# Generated by Django 5.0.2 on 2024-05-06 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_product_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]