# Generated by Django 4.2 on 2023-07-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuati_app', '0006_answerrecord_isinerrorbook_answerrecord_record_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerrecord',
            name='record_id',
            field=models.CharField(default='', max_length=20, verbose_name='题目编号'),
        ),
    ]
