# Generated by Django 3.0.7 on 2020-07-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]