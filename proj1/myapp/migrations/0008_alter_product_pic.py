# Generated by Django 5.0.2 on 2024-03-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
