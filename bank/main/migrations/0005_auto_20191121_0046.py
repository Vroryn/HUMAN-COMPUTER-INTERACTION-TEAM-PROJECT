# Generated by Django 2.2.7 on 2019-11-21 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191121_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='account_balance',
            field=models.IntegerField(default=0),
        ),
    ]