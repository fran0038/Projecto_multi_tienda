# Generated by Django 3.1 on 2022-11-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_productos_imagenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagenes',
            field=models.ImageField(upload_to='imagenes'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
