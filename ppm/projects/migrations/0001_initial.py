# Generated by Django 4.1.7 on 2023-03-13 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("purpose", models.TextField(blank=True)),
                ("success_criteria", models.TextField(blank=True)),
                (
                    "start_date",
                    models.DateField(default=django.utils.datetime_safe.date.today),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("100", "Pending"),
                            ("200", "On Track"),
                            ("300", "Off Track"),
                            ("400", "At Risk"),
                            ("500", "Hold"),
                            ("600", "Completed"),
                        ],
                        default="100",
                        max_length=3,
                    ),
                ),
                ("is_archived", models.BooleanField(default=False)),
                (
                    "assigned_to",
                    models.ManyToManyField(
                        blank=True,
                        related_name="assigned_projects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_projects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sponsor",
                    models.ManyToManyField(
                        blank=True,
                        related_name="sponsored_projects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("summary", models.CharField(max_length=280)),
                ("detail", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("UPDT", "Update"),
                            ("LESL", "Lesson Learned"),
                            ("CHNG", "Change Request"),
                            ("QUES", "Question"),
                            ("EVNT", "Event"),
                            ("THNK", "Thanks"),
                            ("RISK", "Risk"),
                            ("INFO", "Information"),
                        ],
                        max_length=4,
                    ),
                ),
                ("files", models.FileField(blank=True, upload_to="files/")),
                ("image", models.ImageField(blank=True, upload_to="images/")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updates",
                        to="projects.project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
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
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="projects.post"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.CharField(max_length=280)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("file", models.FileField(blank=True, upload_to="")),
                ("image", models.ImageField(blank=True, upload_to="")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="projects.post"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
