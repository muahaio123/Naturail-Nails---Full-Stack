# Generated by Django 4.2.7 on 2023-11-12 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
