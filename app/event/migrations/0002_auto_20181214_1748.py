# Generated by Django 2.1.4 on 2018-12-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('happy', '해피머니 이벤트'), ('join', '참여 이벤트'), ('invite', '초대 이벤트'), ('cashback', '캐시백 이벤트'), ('alliance', '제휴 이벤트'), ('entry', '응모 이벤트'), ('comment', '댓글 이벤트')], max_length=12),
        ),
        migrations.AlterField(
            model_name='event',
            name='tag',
            field=models.CharField(max_length=12),
        ),
    ]
