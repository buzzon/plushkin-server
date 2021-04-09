# Generated by Django 3.2 on 2021-04-09 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_bookmark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
