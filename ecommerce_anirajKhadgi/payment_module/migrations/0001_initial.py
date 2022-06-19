# Generated by Django 4.0.4 on 2022-06-16 02:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentGateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('expiry_date', models.DateField()),
                ('balance', models.FloatField()),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]