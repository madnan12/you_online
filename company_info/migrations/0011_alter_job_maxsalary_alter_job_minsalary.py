# Generated by Django 4.0 on 2022-01-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0010_city_is_deleted_country_is_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='maxsalary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='minsalary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
