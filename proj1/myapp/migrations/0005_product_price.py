# Generated by Django 5.0.2 on 2024-03-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
