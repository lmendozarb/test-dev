# Generated by Django 4.0.2 on 2022-02-04 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='fuel_efficiency',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_tank_size',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilometer', models.IntegerField()),
                ('gas_price', models.PositiveIntegerField()),
                ('left_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_left_stations', to='adventure.servicearea')),
                ('right_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_right_stations', to='adventure.servicearea')),
            ],
        ),
    ]
