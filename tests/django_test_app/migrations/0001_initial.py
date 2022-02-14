# Generated by Django 3.2.12 on 2022-02-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestFieldModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("test_field", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TestFieldWithChoiceModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("test_field", models.IntegerField(choices=[(0, "value0"), (1, "value1")])),
            ],
        ),
        migrations.CreateModel(
            name="TestFieldWithDefaultValueModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("test_field", models.IntegerField(default=-1)),
            ],
        ),
    ]
