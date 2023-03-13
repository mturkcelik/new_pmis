# Generated by Django 4.1.7 on 2023-03-13 14:30

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=280)),
                ('detail', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('UPDT', 'Update'), ('LESL', 'Lesson Learned'), ('CHNG', 'Change Request'), ('QUES', 'Question'), ('EVNT', 'Event'), ('THNK', 'Thanks'), ('RISK', 'Risk'), ('INFO', 'Information')], max_length=4)),
                ('files', models.FileField(blank=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('purpose', models.TextField(blank=True)),
                ('success_criteria', models.TextField(blank=True)),
                ('start_date', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('status', models.CharField(choices=[('100', 'Pending'), ('200', 'On Track'), ('300', 'Off Track'), ('400', 'At Risk'), ('500', 'Hold'), ('600', 'Completed')], default='100', max_length=3)),
                ('is_archived', models.BooleanField(default=False)),
            ],
        ),
    ]
