# Generated by Django 2.2.7 on 2019-12-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0020_auto_20191226_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='final_answer_id',
            field=models.IntegerField(null=True),
        ),
    ]
