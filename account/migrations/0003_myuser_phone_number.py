# Generated by Django 4.0.3 on 2022-04-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_myuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]