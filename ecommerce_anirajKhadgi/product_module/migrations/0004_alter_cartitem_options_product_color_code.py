# Generated by Django 4.0.4 on 2022-06-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_product_registered_on_cartitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name_plural': 'Cart_Items'},
        ),
        migrations.AddField(
            model_name='product',
            name='color_code',
            field=models.CharField(default='', max_length=20),
        ),
    ]
