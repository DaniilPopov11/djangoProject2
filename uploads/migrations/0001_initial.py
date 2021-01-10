# Generated by Django 3.1.5 on 2021-01-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=160)),
                ('item', models.CharField(max_length=160)),
                ('total', models.PositiveIntegerField(max_length=100)),
                ('quantity', models.PositiveIntegerField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
