# Generated by Django 4.2 on 2023-05-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_illustration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="illustration",
            field=models.ImageField(blank=True, null=True, upload_to="posts/"),
        ),
    ]