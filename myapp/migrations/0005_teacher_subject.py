# Generated by Django 4.2.5 on 2023-10-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_rename_curator_group_teacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="subject",
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
