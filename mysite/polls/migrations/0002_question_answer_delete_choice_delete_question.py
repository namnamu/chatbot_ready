# Generated by Django 4.2.3 on 2023-11-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question_Answer",
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
                ("ID", models.CharField(max_length=200)),
                ("user_key", models.CharField(max_length=200)),
                ("Answer", models.CharField(max_length=200)),
                ("upvotes", models.IntegerField(default=0)),
                ("downvotes", models.IntegerField(default=0)),
                ("view_count", models.IntegerField(default=0)),
                ("Keywords", models.CharField(max_length=200)),
                ("Date", models.DateTimeField(verbose_name="date published")),
                ("Links", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="Choice",
        ),
        migrations.DeleteModel(
            name="Question",
        ),
    ]
