# Generated by Django 4.2.5 on 2023-10-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_alter_teacher_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="subject",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
