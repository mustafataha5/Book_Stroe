# Generated by Django 2.2.4 on 2024-05-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0007_auto_20240526_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=7),
        ),
    ]
