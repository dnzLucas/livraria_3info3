# Generated by Django 5.1.7 on 2025-04-22 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_livro_autores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='autores',
        ),
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.autor'),
        ),
    ]
