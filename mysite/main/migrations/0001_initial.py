# Generated by Django 4.2.4 on 2023-08-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=60, verbose_name='Model')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
            ],
        ),
    ]
