# Generated by Django 4.2.13 on 2025-02-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_auto_20230210_1424"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="audit",
            options={
                "ordering": ["data_type", "-created"],
                "verbose_name": "Auditoria",
                "verbose_name_plural": "Auditorias",
            },
        ),
        migrations.AlterField(
            model_name="audit",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="audit",
            name="ip",
            field=models.CharField(max_length=50, verbose_name="IP do Responsável"),
        ),
    ]
