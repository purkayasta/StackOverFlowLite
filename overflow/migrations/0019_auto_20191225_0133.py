# Generated by Django 2.2.7 on 2019-12-24 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0018_auto_20191225_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answervotemodel',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avm_answer', to='overflow.AnswerModel'),
        ),
    ]
