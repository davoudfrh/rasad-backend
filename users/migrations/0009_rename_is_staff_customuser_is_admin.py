# Generated by Django 3.2.8 on 2022-01-26 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
