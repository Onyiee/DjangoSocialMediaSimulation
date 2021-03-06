# Generated by Django 3.2 on 2021-04-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_owner_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='owner',
            name='profile_picture',
            field=models.ImageField(default='teenage(1).png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='owner',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
