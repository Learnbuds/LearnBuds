# Generated by Django 5.0.6 on 2024-05-22 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('U_Auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_customer',
            new_name='is_user',
        ),
    ]
