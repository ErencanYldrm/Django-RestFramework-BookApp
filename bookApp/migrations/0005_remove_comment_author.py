# Generated by Django 4.1.7 on 2023-04-11 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]