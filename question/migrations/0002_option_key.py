# Generated by Django 3.2.4 on 2021-07-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='key',
            field=models.CharField(default='A', max_length=2),
        ),
    ]