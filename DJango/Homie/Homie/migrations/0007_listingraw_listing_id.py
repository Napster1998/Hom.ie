# Generated by Django 4.1.3 on 2022-12-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homie', '0006_alter_listingraw_listing_no_of_bathrooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingraw',
            name='listing_id',
            field=models.CharField(default='', max_length=30),
        ),
    ]
