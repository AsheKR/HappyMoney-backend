# Generated by Django 2.1.4 on 2018-12-12 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0002_auto_20181212_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='happygiftcard',
            name='is_active',
        ),
    ]