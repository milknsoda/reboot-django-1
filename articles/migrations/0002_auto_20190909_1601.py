# Generated by Django 2.2.4 on 2019-09-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
