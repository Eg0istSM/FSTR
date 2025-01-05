# Generated by Django 5.1.4 on 2025-01-05 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.pereval'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
