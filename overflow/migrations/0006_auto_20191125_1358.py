# Generated by Django 2.2.7 on 2019-11-25 07:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0005_auto_20191125_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]