# Generated by Django 4.1.3 on 2022-12-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homie', '0005_alter_listingraw_listing_no_of_bathrooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingraw',
            name='listing_no_of_bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listingraw',
            name='listing_no_of_bedrooms',
            field=models.IntegerField(default=0),
        ),
    ]
