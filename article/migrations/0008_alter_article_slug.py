# Generated by Django 4.2.7 on 2023-12-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
