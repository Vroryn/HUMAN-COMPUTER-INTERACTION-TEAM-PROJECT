# Generated by Django 2.2.7 on 2019-12-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_credit_cardacct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit_cardacct',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
