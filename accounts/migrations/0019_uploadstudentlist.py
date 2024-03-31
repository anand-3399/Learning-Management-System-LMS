# Generated by Django 4.0.8 on 2024-03-24 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_uploadlecturerlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadStudentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='student_list/', validators=[django.core.validators.FileExtensionValidator(['xls', 'xlsx'])])),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
