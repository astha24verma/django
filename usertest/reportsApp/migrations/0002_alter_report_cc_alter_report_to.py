# Generated by Django 5.1 on 2024-08-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='cc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='to',
            field=models.TextField(),
        ),
    ]