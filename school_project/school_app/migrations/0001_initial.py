# Generated by Django 4.2.7 on 2023-11-16 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("name", models.CharField(max_length=255)),
                ("dob", models.DateField()),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=10)),
                ("phone_number", models.CharField(max_length=12)),
                ("mail_id", models.EmailField(max_length=254)),
                ("address", models.TextField(blank=True)),
                ("course", models.CharField(max_length=50)),
                ("purpose", models.CharField(max_length=50)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school_app.department",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school_app.user",
                    ),
                ),
            ],
            options={
                "verbose_name": "User profile",
                "verbose_name_plural": "User profiles",
                "ordering": ("name",),
            },
        ),
    ]
