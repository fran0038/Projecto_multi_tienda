# Generated by Django 3.1 on 2022-11-29 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20221129_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagenes',
            field=models.URLField(),
        ),
    ]
