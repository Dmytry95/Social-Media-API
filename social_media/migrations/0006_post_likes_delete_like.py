# Generated by Django 4.2.3 on 2023-07-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social_media", "0005_post_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="posts_liked", to="social_media.profile"
            ),
        ),
        migrations.DeleteModel(
            name="Like",
        ),
    ]
