# Generated by Django 4.1.3 on 2022-12-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homie', '0008_alter_listingraw_listing_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
