# Generated by Django 4.1 on 2024-04-02 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0005_tbl_size'),
        ('Ownerapp', '0002_alter_tbl_turf_amount_alter_tbl_turf_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_turf',
            name='LocationId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adminapp.tbl_location'),
        ),
    ]
