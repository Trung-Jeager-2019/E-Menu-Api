# Generated by Django 3.1.5 on 2021-01-16 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('image', models.CharField(max_length=2048)),
                ('decribe', models.CharField(max_length=4096)),
            ],
        ),
    ]