# Generated by Django 4.1.7 on 2023-03-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeding',
            old_name='Finch',
            new_name='finch',
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='feeding date'),
        ),
    ]