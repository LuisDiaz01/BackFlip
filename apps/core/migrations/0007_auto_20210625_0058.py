# Generated by Django 3.0.4 on 2021-06-25 00:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210623_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='actualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='club',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='divicion',
            name='name',
            field=models.CharField(choices=[('sub', '12'), ('sub', '14'), ('sub', '16'), ('sub', '18'), ('sub', '21')], max_length=50),
        ),
        migrations.CreateModel(
            name='Encuentro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_de_encuentro', models.CharField(choices=[('A', 'Amistoso'), ('C', 'Clasificatorio'), ('E', 'Estadal'), ('N', 'Nacional')], max_length=50)),
                ('goles_invitado', models.IntegerField(default=0)),
                ('goles_casa', models.IntegerField(default=0)),
                ('equipo_casa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casa', to='core.Equipo')),
                ('equipo_invitado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitado', to='core.Equipo')),
            ],
        ),
    ]