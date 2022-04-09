# Generated by Django 4.0.3 on 2022-04-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_post_city_post_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location_kind',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='rest_place',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]