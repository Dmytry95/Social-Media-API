# Generated by Django 4.2.3 on 2023-07-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social_media", "0008_remove_post_scheduled_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="scheduled_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
