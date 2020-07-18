# Generated by Django 3.0.6 on 2020-05-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BreweryLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brewery_name', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, default='/media/generic_logo.png', null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now=True)),
                ('externalURL', models.URLField(blank=True)),
            ],
        ),
    ]
