# Generated by Django 3.0.5 on 2020-06-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_auto_20200621_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
