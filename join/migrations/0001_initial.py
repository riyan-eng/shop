# Generated by Django 3.2.4 on 2021-12-30 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kelamin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ortu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='anak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(default='')),
                ('jenis_kelamin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='join.kelamin')),
                ('nama_orang_tua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='join.ortu')),
            ],
        ),
    ]