# Generated by Django 3.2 on 2020-07-27 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_posts_views'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
