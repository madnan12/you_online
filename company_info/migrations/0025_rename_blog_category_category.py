# Generated by Django 4.0 on 2022-01-11 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0024_blog_category_blog_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog_Category',
            new_name='Category',
        ),
    ]