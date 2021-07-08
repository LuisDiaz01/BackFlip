# Generated by Django 3.0.4 on 2021-06-25 01:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210625_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuentro',
            name='actualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='encuentro',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encuentro',
            name='estatus',
            field=models.CharField(choices=[('1', 'Pendiente'), ('1', 'Finalizado')], default='Pe', max_length=50),
        ),
    ]
