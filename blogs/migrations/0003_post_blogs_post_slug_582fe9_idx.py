# Generated by Django 4.2 on 2024-02-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_user_comment_author'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['slug'], name='blogs_post_slug_582fe9_idx'),
        ),
    ]
