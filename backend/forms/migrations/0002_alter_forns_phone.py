# Generated by Django 5.0.6 on 2024-07-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forns',
            name='phone',
            field=models.IntegerField(),
        ),
    ]