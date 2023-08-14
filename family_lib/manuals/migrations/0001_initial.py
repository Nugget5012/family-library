# Generated by Django 4.2.4 on 2023-08-12 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_tag', models.CharField(blank=True, max_length=500, null=True)),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.CharField(blank=True, max_length=256, null=True)),
                ('product_model', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('manual_id', models.AutoField(primary_key=True, serialize=False)),
                ('manual_title', models.CharField(max_length=100)),
                ('manual_description', models.CharField(blank=True, max_length=500, null=True)),
                ('manual_url', models.CharField(blank=True, max_length=200, null=True)),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='manuals.product')),
            ],
        ),
    ]