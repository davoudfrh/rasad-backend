# Generated by Django 3.2.8 on 2022-01-26 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_is_staff_customuser_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='token',
        ),
    ]