# Generated by Django 4.0.3 on 2022-05-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
    ]
