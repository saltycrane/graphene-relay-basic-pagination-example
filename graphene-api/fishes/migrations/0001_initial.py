# Generated by Django 3.1.5 on 2021-01-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('icon_url', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]