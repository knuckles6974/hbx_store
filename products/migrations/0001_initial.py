# Generated by Django 4.0.6 on 2022-09-22 11:38

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
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=7)),
                ('sizeguide', models.CharField(max_length=2000)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('interestproduct', models.BooleanField()),
            ],
        ),
    ]
