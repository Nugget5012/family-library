# Generated by Django 4.2.4 on 2023-08-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manual',
            name='manual_file',
            field=models.ImageField(null=True, upload_to='files/covers'),
        ),
    ]