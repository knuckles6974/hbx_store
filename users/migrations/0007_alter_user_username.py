# Generated by Django 4.0.6 on 2022-09-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
