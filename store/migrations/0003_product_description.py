# Generated by Django 4.2.1 on 2023-05-22 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
