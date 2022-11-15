# Generated by Django 4.1.3 on 2022-11-10 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("make", models.CharField(blank=True, max_length=50, null=True)),
                ("os_version", models.CharField(blank=True, max_length=50, null=True)),
                ("model", models.CharField(blank=True, max_length=50, null=True)),
                ("serial_no", models.CharField(blank=True, max_length=50, null=True)),
                ("profile", models.CharField(blank=True, max_length=50, null=True)),
                ("device_id", models.CharField(blank=True, max_length=50, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now_add=True)),
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("mobile_no", models.CharField(blank=True, max_length=20, null=True)),
                ("smc", models.CharField(blank=True, max_length=30, null=True)),
                ("email_id", models.CharField(blank=True, max_length=100, null=True)),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Session",
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
                ("client_key", models.CharField(blank=True, max_length=100, null=True)),
                ("ip_address", models.CharField(blank=True, max_length=50, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "device",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web_app.device",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web_app.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="device",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="web_app.user",
            ),
        ),
    ]
