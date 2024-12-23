# Generated by Django 5.1.4 on 2024-12-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='created_at',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='Not Provided', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
