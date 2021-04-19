# Generated by Django 2.2.13 on 2021-04-19 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_auto_20201123_0957'),
        ('mutations', '0024_strainmutationcache'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strainmutationcache',
            old_name='paper',
            new_name='source_paper',
        ),
        migrations.AlterUniqueTogether(
            name='strainmutationcache',
            unique_together={('mutation', 'importer', 'source_paper', 'country', 'lineage')},
        ),
    ]
