# Generated by Django 4.0 on 2022-01-07 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0015_job_profile_alter_job_experience_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_profile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]