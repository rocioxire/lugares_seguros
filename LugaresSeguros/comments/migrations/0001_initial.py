# Generated by Django 4.0.2 on 2022-07-20 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.place')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
