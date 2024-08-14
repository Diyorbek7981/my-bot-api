# Generated by Django 5.1 on 2024-08-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField()),
                ('github', models.URLField()),
                ('telegram', models.CharField(max_length=100)),
                ('linktee', models.URLField()),
            ],
        ),
    ]
