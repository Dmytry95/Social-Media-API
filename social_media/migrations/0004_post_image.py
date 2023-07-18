# Generated by Django 4.2.3 on 2023-07-18 10:02

from django.db import migrations, models
import social_media.models


class Migration(migrations.Migration):
    dependencies = [
        (
            "social_media",
            "0003_profile_followers_profile_status_profile_username_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=social_media.models.post_pic_file_path
            ),
        ),
    ]