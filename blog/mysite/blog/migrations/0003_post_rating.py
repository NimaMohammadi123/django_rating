# Generated by Django 4.0.1 on 2022-10-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_arthor_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'published')], default='0', max_length=10),
        ),
    ]
