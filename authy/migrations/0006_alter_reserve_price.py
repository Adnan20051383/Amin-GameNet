# Generated by Django 5.1.1 on 2024-10-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0005_alter_reserve_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='price',
            field=models.TextField(blank=True, null=True),
        ),
    ]
