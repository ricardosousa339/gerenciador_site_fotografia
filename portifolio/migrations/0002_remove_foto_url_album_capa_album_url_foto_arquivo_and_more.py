# Generated by Django 4.2.13 on 2025-02-21 20:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import portifolio.files
import portifolio.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0001_initial"),
        ("portifolio", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="foto",
            name="url",
        ),
        migrations.AddField(
            model_name="album",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cover",
                to="portifolio.foto",
            ),
        ),
        migrations.AddField(
            model_name="album",
            name="url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="foto",
            name="arquivo",
            field=models.ImageField(
                blank=True,
                help_text="Arquivo da foto",
                null=True,
                upload_to=portifolio.files.generate_unique_file_name,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["pdf", "jpg", "jpeg", "png"]
                    ),
                    portifolio.validators.FileSizeValidator(max_size=5),
                ],
                verbose_name="Arquivo",
            ),
        ),
        migrations.CreateModel(
            name="ImagemHeader",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("enabled", models.BooleanField(default=True, verbose_name="Ativo")),
                ("deleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "imagem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="header",
                        to="portifolio.foto",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="headers",
                        to="usuario.usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Imagem de Cabeçalho",
                "verbose_name_plural": "Imagens de Cabeçalho",
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("enabled", models.BooleanField(default=True, verbose_name="Ativo")),
                ("deleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nome", models.CharField(max_length=255)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="usuario.usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.AddField(
            model_name="album",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="albums",
                to="portifolio.categoria",
            ),
        ),
    ]
