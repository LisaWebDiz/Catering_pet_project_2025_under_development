# Generated by Django 5.2.2 on 2025-06-11 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cookingtool_dishproduct_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishproduct',
            options={'ordering': ['dish'], 'verbose_name': 'Продукт для блюда', 'verbose_name_plural': 'Продукты для блюда'},
        ),
        migrations.RemoveField(
            model_name='dishproduct',
            name='name',
        ),
    ]
