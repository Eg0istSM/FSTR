# Generated by Django 5.1.4 on 2025-01-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0002_alter_images_pereval_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='pereval',
            name='beauty_title',
            field=models.CharField(default='пер.', max_length=50),
        ),
    ]