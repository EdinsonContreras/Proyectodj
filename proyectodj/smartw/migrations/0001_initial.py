# Generated by Django 4.1.1 on 2022-09-28 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smartband',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('heart_rate', models.IntegerField()),
                ('BPM', models.IntegerField()),
                ('Sp_o', models.IntegerField()),
                ('level_stress', models.IntegerField()),
            ],
        ),
    ]
