# Generated by Django 5.0.7 on 2024-07-12 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'wmv'])])),
            ],
        ),
    ]