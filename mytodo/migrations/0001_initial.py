# Generated by Django 3.0.4 on 2020-12-13 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Did',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Do',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do', models.CharField(max_length=300)),
            ],
        ),
    ]
