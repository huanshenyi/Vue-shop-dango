# Generated by Django 2.0 on 2019-08-19 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='アドレス'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='携帯番号'),
        ),
    ]
