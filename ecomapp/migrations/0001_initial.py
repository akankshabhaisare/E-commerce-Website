# Generated by Django 5.0.6 on 2024-06-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('pdetail', models.CharField(max_length=300)),
                ('cat', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
