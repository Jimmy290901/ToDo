# Generated by Django 3.2.3 on 2021-06-19 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_mytasks_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytasks',
            old_name='user_id',
            new_name='user_Obj',
        ),
    ]
