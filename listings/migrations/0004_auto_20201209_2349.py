# Generated by Django 3.1.4 on 2020-12-09 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20201209_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='company_description',
            new_name='description',
        ),
    ]
