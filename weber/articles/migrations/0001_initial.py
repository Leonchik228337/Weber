# Generated by Django 4.1.4 on 2022-12-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('text', models.TextField()),
                ('time_create', models.DateTimeField(auto_now=True)),
                ('time_change', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
