# Generated by Django 3.2.4 on 2021-07-10 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='udpated',
            new_name='updated',
        ),
    ]
