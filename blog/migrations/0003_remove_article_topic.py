# Generated by Django 2.2.3 on 2019-07-28 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190728_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='topic',
        ),
    ]
