# Generated by Django 3.1.2 on 2020-11-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('francesubdivisions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commune',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
