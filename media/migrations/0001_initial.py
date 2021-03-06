# Generated by Django 4.0.5 on 2022-06-09 03:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('monetization_status', models.IntegerField(choices=[(1, 'On'), (2, 'Off')], default='2')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('dimension', models.CharField(blank=True, max_length=100)),
                ('size', models.CharField(blank=True, max_length=100)),
                ('duration', models.IntegerField(blank=True, verbose_name='Duration in seconds')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('length', models.IntegerField(blank=True, verbose_name='Length in seconds')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('media', models.ManyToManyField(blank=True, to='media.media')),
            ],
        ),
    ]
