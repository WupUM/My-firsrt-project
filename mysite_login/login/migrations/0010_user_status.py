# Generated by Django 4.0.1 on 2022-07-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_rename_usermodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '允许匹配'), (2, '暂时不允许匹配'), (3, '匹配成功')], default=1, verbose_name='匹配状态'),
        ),
    ]
