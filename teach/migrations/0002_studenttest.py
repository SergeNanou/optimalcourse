# Generated by Django 2.2.5 on 2019-09-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=30)),
                ('study', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]