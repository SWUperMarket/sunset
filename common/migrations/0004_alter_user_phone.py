# Generated by Django 4.0.3 on 2024-02-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_user_verifycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
