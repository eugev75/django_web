# Generated by Django 4.1.6 on 2023-02-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="description",
            new_name="Descriptions",
        ),
        migrations.AlterField(
            model_name="task",
            name="datecompleted",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
