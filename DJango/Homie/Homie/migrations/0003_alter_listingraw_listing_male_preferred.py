# Generated by Django 4.1.3 on 2022-12-14 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homie', '0002_alter_listingraw_listing_available_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingraw',
            name='listing_male_preferred',
            field=models.BooleanField(default=False),
        ),
    ]