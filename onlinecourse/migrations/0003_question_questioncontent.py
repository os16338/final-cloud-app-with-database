# Generated by Django 3.1.3 on 2022-10-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20221003_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionContent',
            field=models.CharField(default='', max_length=35),
        ),
    ]