# Generated by Django 4.1.7 on 2023-03-07 10:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_alter_post_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, related_name='assigned_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='sponsor',
            field=models.ManyToManyField(blank=True, related_name='sponsored_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]