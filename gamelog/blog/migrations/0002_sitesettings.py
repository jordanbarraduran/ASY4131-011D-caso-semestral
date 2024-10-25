# Generated by Django 5.1.2 on 2024-10-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_image', models.ImageField(blank=True, null=True, upload_to='hero_images/')),
                ('hero_title', models.CharField(default='Welcome to GameLog', max_length=200)),
                ('hero_subtitle', models.TextField(default='Your gaming community hub for news, reviews, and discussions.')),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Settings',
            },
        ),
    ]