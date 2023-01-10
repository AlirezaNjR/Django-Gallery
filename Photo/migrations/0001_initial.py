# Generated by Django 4.1.4 on 2023-01-10 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('body', models.TextField(default='', max_length=900)),
                ('image', models.ImageField(upload_to='pic/%y,%m,%d')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(blank=True, choices=[('ایران', 'ایران'), ('آمریکا', 'آمریکا'), ('ترکیه', 'ترکیه'), ('روسیه', 'روسیه'), ('کره', 'کره')], max_length=50, null=True)),
                ('photo_grapher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
