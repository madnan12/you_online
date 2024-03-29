# Generated by Django 4.0 on 2022-01-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0014_job_experience_job_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='jobprofile_logo')),
                ('headline', models.CharField(max_length=35)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('about', models.TextField()),
            ],
            options={
                'db_table': 'Job_Profile',
            },
        ),
        migrations.AlterField(
            model_name='job_experience',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job_experience',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job_project',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job_project',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
