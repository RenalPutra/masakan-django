# Generated by Django 4.1.3 on 2022-12-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_masakan"),
    ]

    operations = [
        migrations.AddField(
            model_name="masakan",
            name="idMeal",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
