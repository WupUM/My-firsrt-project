# Generated by Django 4.0.1 on 2022-07-11 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_user_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='status',
            new_name='match_status',
        ),
    ]