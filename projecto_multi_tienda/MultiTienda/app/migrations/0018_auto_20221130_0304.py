# Generated by Django 3.1 on 2022-11-30 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20221130_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='categorias',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.categorias'),
        ),
    ]
