# Generated by Django 3.2.12 on 2022-02-21 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0003_alter_city_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название поезда')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='Время в пути')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city_set', to='cities.city', verbose_name='Из какого города')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set', to='cities.city', verbose_name='В какой город')),
            ],
            options={
                'verbose_name': 'Поезд',
                'verbose_name_plural': 'Поезда',
                'ordering': ['travel_time'],
            },
        ),
    ]
