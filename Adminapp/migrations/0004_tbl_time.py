# Generated by Django 4.1 on 2024-03-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0003_tbl_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_Time',
            fields=[
                ('TimeId', models.AutoField(primary_key=True, serialize=False)),
                ('Time', models.CharField(max_length=50)),
            ],
        ),
    ]
