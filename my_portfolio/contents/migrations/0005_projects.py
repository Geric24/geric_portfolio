# Generated by Django 5.2 on 2025-05-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_rename_ncmodel_ncmodel_nc_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_img', models.ImageField(upload_to='projects_img/')),
            ],
        ),
    ]
