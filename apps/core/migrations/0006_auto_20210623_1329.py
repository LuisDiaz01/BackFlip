# Generated by Django 3.0.4 on 2021-06-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210602_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/directivo', verbose_name='Img'),
        ),
    ]
