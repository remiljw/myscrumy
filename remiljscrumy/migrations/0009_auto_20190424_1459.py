# Generated by Django 2.2 on 2019-04-24 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remiljscrumy', '0008_customuser_unsubscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='subscribe',
            new_name='subscription',
        ),
    ]
