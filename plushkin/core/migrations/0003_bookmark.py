# Generated by Django 3.2 on 2021-04-09 11:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20210409_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('U', 'Unsorted'), ('L', 'Liked'), ('T', 'Trash')], default='U', max_length=1)),
                ('title', models.TextField()),
                ('url', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', related_query_name='bookmark', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]