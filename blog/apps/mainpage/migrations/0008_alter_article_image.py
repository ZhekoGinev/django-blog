# Generated by Django 4.0.3 on 2022-05-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='default.png', height_field='250px', upload_to='', width_field='250px'),
        ),
    ]