# Generated by Django 2.1.4 on 2018-12-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0004_auto_20181214_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergiftcard',
            name='delivery_type',
            field=models.CharField(choices=[('sms', 'SMS'), ('email', 'EMAIL'), ('address', 'address')], max_length=10),
        ),
    ]
