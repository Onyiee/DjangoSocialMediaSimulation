# Generated by Django 3.2 on 2021-04-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
