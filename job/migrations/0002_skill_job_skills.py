# Generated by Django 4.2.7 on 2024-02-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="job",
            name="skills",
            field=models.ManyToManyField(related_name="jobs", to="job.skill"),
        ),
    ]
