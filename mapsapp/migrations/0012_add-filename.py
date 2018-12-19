# Generated by Django 2.1.2 on 2018-12-19 17:44

from django.db import migrations, models


def extract_filename(apps, _):
    Rms = apps.get_model('mapsapp', 'Rms')
    for rms in Rms.objects.all():
        rms.original_filename = rms.file.path.split('/')[-1]
        rms.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mapsapp', '0011_auto_20181025_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='rms',
            name='original_filename',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.RunPython(extract_filename)
    ]
