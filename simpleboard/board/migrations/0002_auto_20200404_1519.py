# Generated by Django 3.0.5 on 2020-04-04 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='creatdts',
            new_name='createdts',
        ),
    ]