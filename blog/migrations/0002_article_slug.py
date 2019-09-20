# Generated by Django 2.2.5 on 2019-09-19 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
