# Generated by Django 2.2.7 on 2019-11-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0003_auto_20191117_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='tag',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
