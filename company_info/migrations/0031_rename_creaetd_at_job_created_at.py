# Generated by Django 4.0 on 2022-01-11 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0030_alter_job_creaetd_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='creaetd_at',
            new_name='created_at',
        ),
    ]
