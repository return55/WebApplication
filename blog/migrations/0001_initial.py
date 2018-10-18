# Generated by Django 2.1.2 on 2018-10-11 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_articolo1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cita', to='blog.Articolo')),
                ('id_articolo2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='è_citato', to='blog.Articolo')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cita',
            unique_together={('id_articolo1', 'id_articolo2')},
        ),
    ]
