# Generated by Django 2.1.5 on 2019-04-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remiljscrumy', '0002_auto_20190415_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumprojectrole',
            name='role',
            field=models.CharField(max_length=50),
        ),
    ]