# Generated by Django 5.0.3 on 2024-03-29 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='allow_comment',
            field=models.BooleanField(default=True),
        ),
    ]
