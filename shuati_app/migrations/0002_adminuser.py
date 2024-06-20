# Generated by Django 4.2 on 2023-07-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuati_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='管理员用户名')),
                ('password', models.CharField(max_length=100, verbose_name='管理员密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]
