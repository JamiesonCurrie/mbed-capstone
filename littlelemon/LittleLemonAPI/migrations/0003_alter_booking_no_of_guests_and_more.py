# Generated by Django 4.2.4 on 2023-09-06 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_alter_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='reservation_slot',
            field=models.IntegerField(),
        ),
    ]
