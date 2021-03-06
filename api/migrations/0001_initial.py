# Generated by Django 3.0.5 on 2020-06-21 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True,
                                            serialize=False, unique=True)),
                ('confirmation_code', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('year', models.IntegerField()),
                ('description', models.CharField(max_length=400)),
                ('category',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                   related_name='titles', to='api.Category')),
                ('genre',
                 models.ManyToManyField(related_name='titles', to='api.Genre')),
            ],
        ),
    ]
