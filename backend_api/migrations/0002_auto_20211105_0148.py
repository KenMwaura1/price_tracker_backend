# Generated by Django 3.2.9 on 2021-11-05 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]