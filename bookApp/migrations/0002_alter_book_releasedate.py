# Generated by Django 4.1.7 on 2023-04-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='releaseDate',
            field=models.DateField(null=True),
        ),
    ]
