# Generated by Django 4.0.1 on 2022-06-30 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_rename_user_id_test1_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='like_total',
        ),
    ]