# Generated by Django 4.1 on 2024-04-20 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0005_tbl_size'),
        ('Ownerapp', '0006_tbl_turf_regdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_turftime',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('TimeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.tbl_time')),
                ('TurfId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ownerapp.tbl_turf')),
            ],
        ),
    ]
