# Generated by Django 2.1.4 on 2018-12-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('category', models.CharField(choices=[('happy', '해피머니 이벤트'), ('join', '참여 이벤트'), ('invite', '초대 이벤트'), ('cashback', '캐시백 이벤트'), ('alliance', '제휴 이벤트'), ('entry', '응모 이벤트'), ('comment', '댓글 이벤트')], max_length=10)),
                ('tag', models.CharField(max_length=10)),
                ('general_image', models.ImageField(upload_to='images/event')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='images/event')),
                ('site_url', models.CharField(blank=True, max_length=200, null=True)),
                ('content_image', models.ImageField(blank=True, null=True, upload_to='images/event')),
            ],
        ),
    ]
