# Generated by Django 5.0.3 on 2024-04-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]