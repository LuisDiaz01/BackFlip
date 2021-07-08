# Generated by Django 3.0.4 on 2021-06-25 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210625_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parrilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divicion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Divicion')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Persona')),
            ],
        ),
        migrations.DeleteModel(
            name='Equipo',
        ),
    ]
