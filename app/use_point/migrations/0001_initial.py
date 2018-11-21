# Generated by Django 2.1.3 on 2018-11-21 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('pin', models.CharField(max_length=18)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GiftCardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_day_limit', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('is_hotdeal', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_online', models.BooleanField(default=False)),
                ('is_fee', models.BooleanField(default=False)),
                ('is_import_point', models.BooleanField(default=False)),
                ('month_pay_limit', models.IntegerField(default=0)),
                ('available_pay_limit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UsePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('site', models.TextField()),
                ('shop_image', models.ImageField(blank=True, null=True, upload_to='shop_image')),
            ],
        ),
        migrations.CreateModel(
            name='UsePointCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='usepoint',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='use_point.UsePointCategory'),
        ),
        migrations.AddField(
            model_name='usepoint',
            name='like_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usepoint',
            name='where_to_use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='use_point.Usage'),
        ),
        migrations.AddField(
            model_name='giftcardtype',
            name='use_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='use_point.UsePoint'),
        ),
        migrations.AddField(
            model_name='giftcard',
            name='gift_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='use_point.GiftCardType'),
        ),
        migrations.AddField(
            model_name='giftcard',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
