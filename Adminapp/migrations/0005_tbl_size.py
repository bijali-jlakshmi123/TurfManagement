# Generated by Django 4.1 on 2024-03-19 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0004_tbl_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_size',
            fields=[
                ('SizeId', models.AutoField(primary_key=True, serialize=False)),
                ('Size', models.CharField(max_length=20)),
                ('Amount', models.BigIntegerField()),
            ],
        ),
    ]
