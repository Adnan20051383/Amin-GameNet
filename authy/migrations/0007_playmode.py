# Generated by Django 5.1.1 on 2024-10-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0006_alter_reserve_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='playMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players_num', models.IntegerField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
