# Generated by Django 5.0.2 on 2024-02-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]