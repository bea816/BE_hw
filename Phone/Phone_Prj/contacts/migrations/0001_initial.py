# Generated by Django 5.0.3 on 2024-04-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone_num', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateField()),
            ],
        ),
    ]
