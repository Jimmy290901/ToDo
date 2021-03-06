# Generated by Django 3.2.3 on 2021-06-14 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('registerDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=300)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
