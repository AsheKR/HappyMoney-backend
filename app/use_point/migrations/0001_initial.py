# Generated by Django 2.1.3 on 2018-11-28 13:36

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
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_fee', models.BooleanField(default=False)),
                ('is_import_point', models.BooleanField(default=False)),
                ('month_pay_limit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UsePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_online', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('site', models.TextField()),
                ('shop_image', models.ImageField(blank=True, null=True, upload_to='images/shop_image')),
            ],
            options={
                'ordering': ['pk'],
            },
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
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='use_point.Usage'),
        ),
        migrations.AlterUniqueTogether(
            name='usepoint',
            unique_together={('name', 'is_online')},
        ),
    ]
