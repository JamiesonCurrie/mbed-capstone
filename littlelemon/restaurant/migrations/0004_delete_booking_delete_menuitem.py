# Generated by Django 4.2.4 on 2023-08-31 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_menu_menuitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]