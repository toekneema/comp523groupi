# Generated by Django 3.1.6 on 2021-02-08 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='name',
            new_name='full_name',
        ),
    ]
