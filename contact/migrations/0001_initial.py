# Generated by Django 3.2.24 on 2024-03-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=256)),
                ('order_number', models.CharField(blank=True, max_length=32, null=True)),
                ('subject', models.CharField(choices=[(1, 'Return'), (2, 'Item Not Delivered'), (3, 'Other')], max_length=25)),
                ('reason_for_contact', models.TextField()),
            ],
        ),
    ]