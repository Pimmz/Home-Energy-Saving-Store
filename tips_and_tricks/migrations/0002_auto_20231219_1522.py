# Generated by Django 3.2.23 on 2023-12-19 15:22

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tips_and_tricks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipsandtricks',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipsandtricks',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tipsandtricks',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='tipsandtricks',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tipsandtricks',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tipsandtricks',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='tipsandtricks',
            name='title',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='ApprovalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tips_and_tricks.tipsandtricks')),
            ],
        ),
    ]