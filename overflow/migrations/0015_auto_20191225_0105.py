# Generated by Django 2.2.7 on 2019-12-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0014_auto_20191223_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionvotemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]