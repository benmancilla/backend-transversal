# Generated by Django 5.0.6 on 2024-07-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_react_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='react',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]