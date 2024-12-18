# Generated by Django 4.1 on 2024-12-17 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_owner_commentary_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.post",
            ),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
